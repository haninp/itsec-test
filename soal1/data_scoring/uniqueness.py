import duckdb
import argparse
import os
from datetime import datetime
import csv
from tqdm import tqdm
from schema_metadata import candidate_keys

parser = argparse.ArgumentParser(description="Data Uniqueness Scoring")
parser.add_argument("--input", required=True, help="Path ke file CSV input")
parser.add_argument("--output", required=True, help="Path untuk menyimpan hasil CSV report")
args = parser.parse_args()

csv_path = args.input
output_file = args.output
today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

con = duckdb.connect()
con.execute(f"""
    CREATE OR REPLACE VIEW cybersecurity_logs AS
    SELECT * FROM read_csv_auto('{csv_path}', HEADER=TRUE)
""")

total_rows = con.execute("SELECT COUNT(*) FROM cybersecurity_logs").fetchone()[0]

results = []

for key_cols in tqdm(candidate_keys, desc="Scoring Uniqueness"):
    key_label = " + ".join(key_cols)
    concat_expr = " || '|' || ".join([f'COALESCE(CAST("{col}" AS VARCHAR), \'\')' for col in key_cols])
    dedup_query = f'''
        SELECT COUNT(*) AS total,
            COUNT(DISTINCT {concat_expr}) AS unique_rows
        FROM cybersecurity_logs
    '''
    total, unique_rows = con.execute(dedup_query).fetchone()
    dup_count = total - unique_rows
    score = round((unique_rows / total) * 100, 2)
    status = "PASS" if score == 100.0 else "WARN" if score >= 95 else "FAILED"
    results.append([today, key_label, total, unique_rows, dup_count, score, status])

# Tulis ke CSV
with open(output_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        "Tanggal Scoring", "Kombinasi Kolom", "Total Baris", "Baris Unik",
        "Jumlah Duplikat", "Uniqueness Score (%)", "Status"
    ])
    writer.writerows(results)

# Simpan baris duplikat ke file tambahan
for key_cols in candidate_keys:
    key_label = "_".join([k.replace(" ", "_") for k in key_cols])
    raw_output_path = output_file.replace(".csv", f"_{key_label}_duplicates.csv")
    quoted_cols = [f'"{c}"' for c in key_cols]
    dup_query = f'''
        SELECT * FROM cybersecurity_logs
        WHERE ({', '.join(quoted_cols)}) IN (
            SELECT {', '.join(quoted_cols)}
            FROM cybersecurity_logs
            GROUP BY {', '.join(quoted_cols)}
            HAVING COUNT(*) > 1
        )
    '''
    df = con.execute(dup_query).df()
    if not df.empty:
        df.to_csv(raw_output_path, index=False)
        print(f"⚠️  Duplikat berdasarkan {key_label} disimpan di: {raw_output_path}")

print(f"✅ Laporan uniqueness disimpan di: {output_file}")