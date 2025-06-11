import duckdb
import argparse
import os
import time
from bl_checker import is_blacklisted, load_cache, save_cache
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Run RBL check on unique IPs in dataset")
parser.add_argument("--input", required=True, help="Path ke file CSV input")
args = parser.parse_args()

csv_path = args.input
input_dir = os.path.dirname(csv_path)
rbl_cache_path = os.path.join(input_dir, "rbl_cache.json")

# Buka CSV dengan DuckDB
con = duckdb.connect()
con.execute(f"""
    CREATE OR REPLACE VIEW logs AS
    SELECT * FROM read_csv_auto('{csv_path}', HEADER=TRUE)
""")

# Ambil IP unik dari kolom Source dan Destination IP
source_ips = con.execute("SELECT DISTINCT \"Source IP Address\" FROM logs").fetchall()
dest_ips = con.execute("SELECT DISTINCT \"Destination IP Address\" FROM logs").fetchall()
all_ips = {ip for (ip,) in source_ips + dest_ips if ip}

# Load cache
rbl_cache = load_cache(rbl_cache_path)

# Mulai cek RBL
start_time = time.time()
print(f"🔍 Mengecek {len(all_ips)} IP unik terhadap RBL...")

hit = 0
for ip in tqdm(all_ips, desc="Checking IPs against RBL"):
    if is_blacklisted(ip, rbl_cache):
        hit += 1

elapsed = time.time() - start_time
print(f"\n✅ RBL checking selesai dalam {elapsed:.2f}s.")
print(f"📌 Total IP terdeteksi di RBL: {hit}")
print(f"💾 Cache disimpan di: {rbl_cache_path}")

# Simpan cache
save_cache(rbl_cache, rbl_cache_path)