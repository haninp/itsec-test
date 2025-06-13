import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--dimension", required=True, help="Script scoring yang akan dijalankan (misal: completeness.py)")
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

# Bangun command dan jalankan
cmd = ["python", args.dimension, "--input", args.input, "--output", args.output]
subprocess.run(cmd)