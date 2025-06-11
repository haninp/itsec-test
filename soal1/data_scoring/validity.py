import duckdb
from datetime import datetime
import csv
import argparse
import os
from tqdm import tqdm
from schema_metadata import columns_metadata
from bl_checker import load_cache  # hanya pakai load_cache saja

parser = argparse.ArgumentParser(description="Data Validity Scoring")
parser.add_argument("--input", required=True, help="Path ke file CSV input")
parser.add_argument("--output", required=True, help="Path untuk menyimpan hasil CSV report")
args = parser.parse_args()

csv_path = args.input
output_file = args.output

# Otomatis tentukan path cache di folder yang sama dengan input
input_dir = os.path.dirname(csv_path)
rbl_cache_path = os.path.join(input_dir, "rbl_cache.json")

WARN_THRESHOLD = 90.0
today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

con = duckdb.connect()
con.execute(f"""
    CREATE OR REPLACE VIEW cybersecurity_logs AS
    SELECT
        row_number() OVER () AS row_num,
        *
    FROM read_csv_auto('{csv_path}', HEADER=TRUE)
""")

total_rows = con.execute("SELECT COUNT(*) FROM cybersecurity_logs").fetchone()[0]
rbl_cache = load_cache(rbl_cache_path)

results = []
warn_fail_columns = []

for col, meta in tqdm(columns_metadata.items(), desc="Scoring Validity"):
    validity_sql = meta["validity"]
    invalid_count = con.execute(
        f"SELECT COUNT(*) FROM cybersecurity_logs WHERE NOT coalesce(({validity_sql}), FALSE)"
    ).fetchone()[0]

    valid_count = total_rows - invalid_count
    score = round((valid_count / total_rows) * 100, 2)

    # RBL check (pakai cache saja)
    rbl_hits = 0
    if col in ["Source IP Address", "Destination IP Address"]:
        ip_rows = con.execute(f"SELECT \"{col}\" FROM cybersecurity_logs").fetchall()
        for (ip,) in ip_rows:
            if ip and str(ip) in rbl_cache and rbl_cache[str(ip)].get("blacklisted", False):
                rbl_hits += 1
        if rbl_hits > 0:
            score -= round((rbl_hits / total_rows) * 100, 2)
            invalid_count += rbl_hits
            valid_count = max(0, total_rows - invalid_count)
            score = max(0.0, round((valid_count / total_rows) * 100, 2))

    if not meta["nullable"] and invalid_count > 0:
        status = "FAILED"
    elif meta["nullable"] and score < WARN_THRESHOLD:
        status = "WARN"
    else:
        status = "PASS"

    if status in ("WARN", "FAILED"):
        warn_fail_columns.append(col)

    results.append([
        today,
        col,
        total_rows,
        invalid_count,
        valid_count,
        score,
        status
    ])

# Simpan CSV report
with open(output_file, mode='w', newline='') as f:
    writer = csv.writer(f)

    # Total score
    average_score = round(sum(r[5] for r in results) / len(results), 2)
    writer.writerow(["TOTAL_SCORE : ", average_score])
    writer.writerow([
        "Tanggal Scoring", "Nama Kolom", "Jumlah Total Baris",
        "Jumlah Invalid", "Jumlah Valid", "Validity Score (%)", "Status"
    ])
    writer.writerows(results)

# Simpan baris mentah jika WARN/FAILED
if warn_fail_columns:
    raw_query_conditions = []
    for c in warn_fail_columns:
        if not columns_metadata[c]["nullable"]:
            raw_query_conditions.append(f"NOT coalesce(({columns_metadata[c]['validity']}), FALSE)")
    raw_query = f"""
        SELECT * FROM cybersecurity_logs
        WHERE {" OR ".join(raw_query_conditions)}
    """
    raw_output_path = output_file.replace(".csv", "_records.csv")

    # Buat satu kolom berisi daftar nama kolom yang invalid per baris
    violation_map = {}  # key: row index, value: list of violated columns

    for col in [c for c in warn_fail_columns if not columns_metadata[c]["nullable"]]:
        validity_sql = columns_metadata[col]["validity"]
        query = f'''
            SELECT row_num,
                NOT coalesce(({validity_sql}), FALSE) AS is_invalid
            FROM cybersecurity_logs
        '''
        df = con.execute(query).df()
        # Konversi NA ke False agar mudah dipakai pada logika if
        df["is_invalid"] = df["is_invalid"].fillna(False)
        for _, row in df.iterrows():
            if bool(row["is_invalid"]) is True:
                violation_map.setdefault(row["row_num"], []).append(col)

    # Tambahan: deteksi baris dengan IP yang masuk RBL
    for ip_col in ["Source IP Address", "Destination IP Address"]:
        if ip_col not in warn_fail_columns:
            continue
        ip_rows = con.execute(f"SELECT row_num, \"{ip_col}\" FROM cybersecurity_logs").fetchall()
        for row_num, ip in ip_rows:
            if ip and str(ip) in rbl_cache and rbl_cache[str(ip)].get("blacklisted", False):
                violation_map.setdefault(row_num, []).append(f"{ip_col} (RBL)")

    # Tambahan: deteksi device info yang mencurigakan (misalnya MSIE 5.0)
    dev_rows = con.execute('SELECT row_num, "Device Information" FROM cybersecurity_logs').fetchall()
    for row_num, ua in dev_rows:
        if ua and "MSIE 5.0" in ua:
            violation_map.setdefault(row_num, []).append("Device Information (Suspect Bot)")

    # Ambil ulang seluruh baris raw
    full_df = con.execute("SELECT row_num, * FROM cybersecurity_logs").df()
    full_df["Invalid Columns"] = full_df["row_num"].apply(lambda rid: ", ".join(violation_map.get(rid, [])))
    full_df["Invalid Columns"] = full_df["Invalid Columns"].fillna('')
    warn_fail_rows = full_df[full_df["Invalid Columns"].str.strip() != ""].drop(columns=["row_num"])

    warn_fail_rows.to_csv(raw_output_path, index=False)
    print(f"⚠️  Baris data raw (WARN/FAILED) disimpan di: {raw_output_path}")

print(f"✅ Validity report berhasil disimpan di: {output_file}")