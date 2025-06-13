FROM python:3.13-slim

WORKDIR /app

# Install dependensi sistem
# Pisahkan runtime dan build dependencies
# RUN pip install --upgrade pip \
#     && pip install --no-cache-dir \
#     pandas pyarrow requests numpy boto3

# Buat folder file
RUN mkdir -p file

# Salin file aplikasi dari host ke container
COPY ./soal1/csv_newline_fixer/csv_newline_fixer.py .

ENTRYPOINT ["python", "csv_newline_fixer.py"]
# CMD ["python", "csv_newline_fixer.py"]


# docker build -t csv_newline_fixer:0 .