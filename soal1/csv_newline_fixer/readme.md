# CSV Newline Fixer

Objective : Fixing CSV common problem of newline characters in the field text.

Used the script:
```bash
# Perbaiki data.csv, output otomatis ke data_fixed.csv
python csv_newline_fixer.py cybersecurity_attacks.csv

# Perbaiki dengan output custom
python fix_csv_newline_fixercsv.py cybersecurity_attacks.csv -o data_fixed.csv

# Perbaiki dengan jumlah kolom spesifik dan preview 10 baris
python csv_newline_fixer.py cybersecurity_attacks.csv -c 8 -p 10

# Perbaiki tanpa konfirmasi (otomatis yes)
python csv_newline_fixer.py cybersecurity_attacks.csv -y

# Lihat help
python csv_newline_fixer.py -h
```

Used the script with docker:
```bash
# go to root folder
# build the image
docker build \
	-f soal1/csv_newline_fixer/Dockerfile \
	--platform linux/arm64 \
	-t csv_newline_fixer:0 .

# run the following command
docker run --rm \
    -v "./soal1/file:/app/file" \
    csv_newline_fixer:0 \
    file/cybersecurity_attacks.csv -y
```

Parameter yang tersedia:

- input_file (wajib) - Path ke file CSV yang akan diperbaiki
- -o, --output - Path file output (default: input_file_fixed.csv)
- -c, --columns - Jumlah kolom yang diharapkan (opsional, auto-detect jika tidak disebutkan)
- -p, --preview - Jumlah baris untuk preview (default: 5)
- -y, --yes - Skip konfirmasi, langsung perbaiki file