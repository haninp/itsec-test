import duckdb
import json
import argparse
import os
import random
import time

# Argument CLI
parser = argparse.ArgumentParser(description="Generate dummy RBL cache for testing")
parser.add_argument("--input", required=True, help="Path ke file CSV input")
parser.add_argument("--output", required=False, help="Path ke file cache output (default: dummy_rbl_cache.json di folder input)")
parser.add_argument("--blacklist-rate", type=float, default=0.03, help="Persentase IP yang disimulasikan sebagai blacklisted (default: 0.03 / 3%)")
args = parser.parse_args()

# Path input/output
csv_path = args.input
output_path = args.output or os.path.join(os.path.dirname(csv_path), "dummy_rbl_cache.json")
rate = args.blacklist_rate

# Ambil IP dari CSV
con = duckdb.connect()
con.execute(f"""
    CREATE OR REPLACE VIEW logs AS
    SELECT * FROM read_csv_auto('{csv_path}', HEADER=TRUE)
""")

source_ips = con.execute("SELECT DISTINCT \"Source IP Address\" FROM logs").fetchall()
dest_ips = con.execute("SELECT DISTINCT \"Destination IP Address\" FROM logs").fetchall()
all_ips = {ip for (ip,) in source_ips + dest_ips if ip}

# Buat cache dummy
now = time.time()
dummy_cache = {}
for ip in all_ips:
    dummy_cache[ip] = {
        "blacklisted": random.random() < rate,
        "checked_at": now
    }

# Simpan ke file
with open(output_path, "w") as f:
    json.dump(dummy_cache, f, indent=2)

# Log
print(f"✅ Dummy RBL cache disimpan di: {output_path}")
print(f"📦 Total IP unik: {len(all_ips)}")
print(f"🚩 Jumlah IP disimulasikan sebagai blacklisted: {sum(1 for v in dummy_cache.values() if v['blacklisted'])} (rate={rate})")