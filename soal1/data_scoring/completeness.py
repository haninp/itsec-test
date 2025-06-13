import duckdb
from datetime import datetime
import csv
import argparse
import os
from tqdm import tqdm
from schema_metadata import columns_metadata

parser = argparse.ArgumentParser(description="Data Completeness Scoring")
parser.add_argument("--input", required=True, help="Path ke file CSV input")
parser.add_argument("--output", required=True, help="Path untuk menyimpan hasil CSV report")
args = parser.parse_args()

csv_path = args.input
output_file = args.output

WARN_THRESHOLD = 90.0
today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

con = duckdb.connect()
con.execute(f"""
    CREATE OR REPLACE VIEW cybersecurity_logs AS
    SELECT * FROM read_csv_auto('{csv_path}', HEADER=TRUE)
""")

total_rows = con.execute("SELECT COUNT(*) FROM cybersecurity_logs").fetchone()[0]
results = []
warn_fail_columns = []

for col, meta in tqdm(columns_metadata.items(), desc="Scoring Completeness"):
    is_nullable = meta["nullable"]
    is_string = col not in ["Source Port", "Destination Port", "Packet Length", "Anomaly Scores"]

    if is_string:
        query = f"""
            SELECT COUNT(*) FROM cybersecurity_logs
            WHERE TRIM(CAST("{col}" AS VARCHAR)) = '' OR "{col}" IS NULL
        """
    else:
        query = f"""
            SELECT COUNT(*) FROM cybersecurity_logs
            WHERE "{col}" IS NULL
        """

    null_count = con.execute(query).fetchone()[0]
    not_null_count = total_rows - null_count
    score = round((not_null_count / total_rows) * 100, 2)

    if not is_nullable and null_count > 0:
        status = "FAILED"
    elif is_nullable and score < WARN_THRESHOLD:
        status = "WARN"
    else:
        status = "PASS"

    if status in ("FAILED"):
        warn_fail_columns.append((col, is_string))

    results.append([
        today,
        col,
        total_rows,
        null_count,
        not_null_count,
        score,
        status
    ])

with open(output_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    
    # Total score
    average_score = round(sum(r[5] for r in results) / len(results), 2)
    writer.writerow(["TOTAL_SCORE : ", average_score])
    writer.writerow([
        "Tanggal Scoring", "Nama Kolom", "Jumlah Total Baris",
        "Jumlah Null", "Jumlah Tidak Null", "Score (%)", "Status"
    ])
    writer.writerows(results)

# Simpan baris mentah jika FAILED
if warn_fail_columns:
    conditions = []
    for col, is_string in warn_fail_columns:
        if is_string:
            conditions.append(f'TRIM(CAST("{col}" AS VARCHAR)) = \'\' OR "{col}" IS NULL')
        else:
            conditions.append(f'"{col}" IS NULL')

    raw_query = f"SELECT * FROM cybersecurity_logs WHERE {' OR '.join(conditions)}"
    raw_output_path = output_file.replace(".csv", "_records.csv")
    warn_fail_rows = con.execute(raw_query).df()
    warn_fail_rows.to_csv(raw_output_path, index=False)
    print(f"⚠️  Baris data raw (FAILED) disimpan di: {raw_output_path}")

print(f"✅ Laporan DQ DuckDB (completeness) disimpan di: {output_file}")