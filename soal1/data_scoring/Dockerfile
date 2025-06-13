FROM python:3.13-slim

WORKDIR /app

# # Install dependensi sistem
# # Pisahkan runtime dan build dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir \
    duckdb dnspython numpy pandas tqdm

# # Buat folder file
RUN mkdir -p file

# # Salin file aplikasi dari host ke container
COPY ./soal1/data_scoring/*.py .

ENTRYPOINT ["python", "runner.py"]
# CMD ["python", "completeness.py"]


# # docker build -t data_scoring:0 .