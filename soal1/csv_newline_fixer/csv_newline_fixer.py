import csv
import re
import argparse
import os

def fix_csv_newlines(input_file, output_file, expected_columns=None):
    """
    Memperbaiki CSV yang rusak karena newline di dalam field text.
    
    Args:
        input_file (str): Path ke file CSV input
        output_file (str): Path ke file CSV output yang sudah diperbaiki
        expected_columns (int): Jumlah kolom yang diharapkan (opsional)
    """
    
    with open(input_file, 'r', encoding='utf-8', newline='') as infile:
        lines = infile.readlines()
    
    if not lines:
        print("File kosong!")
        return
    
    # Deteksi delimiter dan jumlah kolom dari header
    first_line = lines[0].strip()
    delimiter = detect_delimiter(first_line)
    
    if expected_columns is None:
        expected_columns = len(first_line.split(delimiter))
    
    print(f"Delimiter terdeteksi: '{delimiter}'")
    print(f"Jumlah kolom yang diharapkan: {expected_columns}")
    
    fixed_lines = []
    current_line = ""
    
    for i, line in enumerate(lines):
        line = line.rstrip('\n\r')
        current_line += line
        
        # Hitung jumlah kolom dalam baris saat ini
        # Menggunakan regex untuk menghitung delimiter yang tidak ada dalam quotes
        column_count = count_delimiters_outside_quotes(current_line, delimiter) + 1
        
        if column_count >= expected_columns:
            # Baris sudah lengkap, tambahkan ke hasil
            fixed_lines.append(current_line)
            current_line = ""
        else:
            # Baris belum lengkap, tambahkan spasi untuk mengganti newline
            current_line += " "
    
    # Tambahkan baris terakhir jika ada
    if current_line.strip():
        fixed_lines.append(current_line.strip())
    
    # Tulis hasil ke file output
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        for line in fixed_lines:
            outfile.write(line + '\n')
    
    print(f"File diperbaiki! Input: {len(lines)} baris -> Output: {len(fixed_lines)} baris")
    print(f"File hasil disimpan di: {output_file}")

def detect_delimiter(line):
    """Deteksi delimiter CSV (koma, semicolon, atau tab)"""
    delimiters = [',', ';', '\t']
    delimiter_counts = {}
    
    for delim in delimiters:
        delimiter_counts[delim] = line.count(delim)
    
    # Pilih delimiter dengan jumlah terbanyak
    return max(delimiter_counts, key=delimiter_counts.get)

def count_delimiters_outside_quotes(line, delimiter):
    """Hitung jumlah delimiter yang tidak berada di dalam quotes"""
    count = 0
    in_quotes = False
    quote_char = None
    
    i = 0
    while i < len(line):
        char = line[i]
        
        if not in_quotes and char in ['"', "'"]:
            in_quotes = True
            quote_char = char
        elif in_quotes and char == quote_char:
            # Cek jika ada quote ganda (escaped quote)
            if i + 1 < len(line) and line[i + 1] == quote_char:
                i += 1  # Skip escaped quote
            else:
                in_quotes = False
                quote_char = None
        elif not in_quotes and char == delimiter:
            count += 1
        
        i += 1
    
    return count

def preview_fix(input_file, num_lines=5):
    """Preview beberapa baris pertama untuk melihat hasil perbaikan"""
    print(f"\n=== PREVIEW {num_lines} BARIS PERTAMA ===")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    delimiter = detect_delimiter(lines[0].strip())
    expected_columns = len(lines[0].strip().split(delimiter))
    
    current_line = ""
    fixed_count = 0
    
    for line in lines:
        if fixed_count >= num_lines:
            break
            
        line = line.rstrip('\n\r')
        current_line += line
        
        column_count = count_delimiters_outside_quotes(current_line, delimiter) + 1
        
        if column_count >= expected_columns:
            print(f"Baris {fixed_count + 1}: {current_line}")
            current_line = ""
            fixed_count += 1
        else:
            current_line += " "

def main():
    parser = argparse.ArgumentParser(description='Memperbaiki CSV yang rusak karena newline di dalam field text')
    parser.add_argument('input_file', help='Path ke file CSV input yang akan diperbaiki')
    parser.add_argument('-o', '--output', help='Path ke file CSV output (default: input_file_fixed.csv)')
    parser.add_argument('-c', '--columns', type=int, help='Jumlah kolom yang diharapkan (opsional)')
    parser.add_argument('-p', '--preview', type=int, default=5, help='Jumlah baris untuk preview (default: 5)')
    parser.add_argument('-y', '--yes', action='store_true', help='Skip konfirmasi, langsung perbaiki file')
    
    args = parser.parse_args()
    
    input_csv = args.input_file
    
    # Generate output filename jika tidak disediakan
    if args.output:
        output_csv = args.output
    else:
        name, ext = os.path.splitext(input_csv)
        output_csv = f"{name}_fixed{ext}"
    
    try:
        # Cek apakah file input ada
        if not os.path.exists(input_csv):
            print(f"Error: File '{input_csv}' tidak ditemukan!")
            return
        
        # Preview sebelum perbaikan
        print(f"INPUT FILE: {input_csv}")
        print("PREVIEW FILE SEBELUM DIPERBAIKI:")
        with open(input_csv, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i < args.preview:
                    print(f"Baris {i+1}: {line.strip()}")
                else:
                    break
        
        # Preview hasil perbaikan
        preview_fix(input_csv, args.preview)
        
        # Konfirmasi sebelum memperbaiki (skip jika --yes)
        if not args.yes:
            response = input(f"\nLanjutkan memperbaiki file ke '{output_csv}'? (y/n): ")
            if response.lower() not in ['y', 'yes', 'ya']:
                print("Dibatalkan.")
                return
        
        # Perbaiki CSV
        fix_csv_newlines(input_csv, output_csv, args.columns)
        
        print(f"\n=== PREVIEW FILE HASIL ({output_csv}) ===")
        with open(output_csv, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i < args.preview:
                    print(f"Baris {i+1}: {line.strip()}")
                else:
                    break
                    
    except FileNotFoundError:
        print(f"Error: File '{input_csv}' tidak ditemukan!")
    except Exception as e:
        print(f"Error: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    main()
