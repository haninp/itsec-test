# itsec-test

## part 1
Take-Home Test Question: Cybersecurity Attack Data Quality Assessment

Dataset: https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks

Your Task:
- Perform a data quality assessment on the dataset
- Explain any issue(s) founded
- Clean the data (if necessary)
- Interpret the data, including any anomaly or possible security issue(s)
---

### Data Quality & Security Insight Assessment Report

#### 1.Executive Summary

#### 2.Introduction
##### 2.1.Objective(s)
##### 2.2.Scope analysis
##### 2.3.Relevansi

#### 3.Dataset Overview
- Data source - [kaggle data-security-attacks](https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks)
- Amount of data - 40,000 rows
-   <details>
    <summary>cybersecurity_attacks_fixed.csv</summary>

    ```csv
    Timestamp,Source IP Address,Destination IP Address,Source Port,Destination Port,Protocol,Packet Length,Packet Type,Traffic Type,Payload Data,Malware Indicators,Anomaly Scores,Alerts/Warnings,Attack Type,Attack Signature,Action Taken,Severity Level,User Information,Device Information,Network Segment,Geo-location Data,Proxy Information,Firewall Logs,IDS/IPS Alerts,Log Source
    2023-05-30 06:33:58,103.216.15.12,84.9.164.252,31225,17616,ICMP,503,Data,HTTP,"Qui natus odio asperiores nam. Optio nobis iusto accusamus ad perferendis esse at. Asperiores neque at ad. Maiores possimus ipsum saepe vitae. Ad possimus veritatis.",IoC Detected,28.67,,Malware,Known Pattern B,Logged,Low,Reyansh Dugal,Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/5.0),Segment A,"Jamshedpur, Sikkim",150.9.97.135,Log Data,,Server
    2020-08-26 07:08:30,78.199.217.198,66.191.137.154,17245,48166,ICMP,1174,Data,HTTP,"Aperiam quos modi officiis veritatis rem. Omnis nulla dolore perspiciatis. Illo animi mollitia vero voluptates error ad. Quidem maxime eaque optio a. Consectetur quasi veniam et totam culpa ullam.",IoC Detected,51.5,,Malware,Known Pattern A,Blocked,Low,Sumer Rana,Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0),Segment B,"Bilaspur, Nagaland",,Log Data,,Firewall
    2022-11-13 08:23:25,63.79.210.48,198.219.82.17,16811,53600,UDP,306,Control,HTTP,Perferendis sapiente vitae soluta. Hic delectus quae nemo ea esse est rerum.,IoC Detected,87.42,Alert Triggered,DDoS,Known Pattern B,Ignored,Low,Himmat Karpe,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0),Segment C,"Bokaro, Rajasthan",114.133.48.179,Log Data,Alert Data,Firewall
    2023-07-02 10:38:46,163.42.196.10,101.228.192.255,20018,32534,UDP,385,Data,HTTP,Totam maxime beatae expedita explicabo porro labore. Minima ab fugit officiis dicta perspiciatis pariatur. Facilis voluptates eligendi dolores eveniet deserunt. Eveniet reprehenderit culpa quo.,,15.79,Alert Triggered,Malware,Known Pattern B,Blocked,Medium,Fateh Kibe,Mozilla/5.0 (Macintosh; PPC Mac OS X 10_11_5; rv:1.9.6.20) Gecko/2583-02-14 13:30:10 Firefox/11.0,Segment B,"Jaunpur, Rajasthan",,,Alert Data,Firewall
    2023-07-16 13:11:07,71.166.185.76,189.243.174.238,6131,26646,TCP,1462,Data,DNS,"Odit nesciunt dolorem nisi iste iusto. Animi voluptates soluta quis doloribus quas. Iure harum nihil hic illo repellendus. Quia illo fugit eligendi doloremque. In doloremque autem iure.",,0.52,Alert Triggered,DDoS,Known Pattern B,Blocked,Low,Dhanush Chad,Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 6.2; Trident/3.0),Segment C,"Anantapur, Tripura",149.6.110.119,,Alert Data,Firewall
    2022-10-28 13:14:27,198.102.5.160,147.190.155.133,17430,52805,UDP,1423,Data,HTTP,Repellat quas illum harum fugit incidunt exercitationem illum. Voluptate asperiores aperiam magnam eius. Eos quis repellat eos.,,5.76,,Malware,Known Pattern A,Logged,Medium,Zeeshan Viswanathan,Opera/8.58.(X11; Linux i686; nl-NL) Presto/2.9.170 Version/12.00,Segment C,"Aurangabad, Meghalaya",,,,Server
    ```

    </details>

#### 4.Data Quality Assessment
##### 4.1.Completeness

Penilaian kelengkapan dilakukan dengan mengukur keberadaan nilai null atau kosong pada setiap kolom berdasarkan karakteristik datanya. Kolom yang bersifat mandatory seperti Timestamp, Source IP Address, hingga Severity Level diharuskan memiliki isian lengkap untuk memastikan log dapat diinterpretasikan dengan benar dalam konteks keamanan.

Berdasarkan analisis, beberapa kolom bersifat optional (nullable), seperti Payload Data atau Proxy Information, karena tidak semua traffic mencatat informasi tersebut. Namun, kami tetap melakukan evaluasi presentase kelengkapannya untuk mengidentifikasi potensi kesenjangan observabilitas.

Berikut ini adalah tabel penilaian kelengkapan (completeness) kolom yang kami gunakan sebagai rujukan berdasarkan hasil observasi dan praktik umum dalam log data cybersecurity:

| Kolom                   | Nullable? | Alasan                                                                 |
|-------------------------|-----------|------------------------------------------------------------------------|
| `Timestamp`             | ❌ No     | Waktu kejadian log sangat krusial untuk semua analisis                 |
| `Source IP Address`     | ❌ No     | Diperlukan untuk identifikasi sumber serangan                          |
| `Destination IP Address`| ❌ No     | Diperlukan untuk tahu target serangan                                  |
| `Source Port`           | ❌ No     | Bagian penting dari 5-tuple koneksi jaringan                           |
| `Destination Port`      | ❌ No     | Sama pentingnya dengan source port                                     |
| `Protocol`              | ❌ No     | Dibutuhkan untuk interpretasi komunikasi (TCP/UDP/ICMP)                |
| `Packet Length`         | ❌ No     | Ukuran trafik adalah metrik dasar dalam analisis                       |
| `Packet Type`           | ❌ No     | Digunakan untuk klasifikasi dan parsing paket                          |
| `Traffic Type`          | ❌ No     | Penting untuk identifikasi service/port (e.g., HTTP, DNS)              |
| `Attack Type`           | ❌ No     | Label penting untuk klasifikasi insiden                                |
| `Attack Signature`      | ❌ No     | Diperlukan untuk korelasi dengan rule signature (IDS/IPS)              |
| `Action Taken`          | ❌ No     | Menunjukkan hasil dari deteksi/prevention (e.g., blocked/logged)      |
| `Severity Level`        | ❌ No     | Dibutuhkan untuk penilaian dampak dan prioritas penanganan             |
| `Payload Data`          | ✅ Yes    | Bisa kosong jika payload disaring atau tidak dicapture                 |
| `Malware Indicators`    | ✅ Yes    | Hanya muncul jika ada indikator malware terdeteksi                     |
| `Anomaly Scores`        | ✅ Yes    | Tidak semua sistem punya anomaly scoring                              |
| `Alerts/Warnings`       | ✅ Yes    | Kosong jika tidak ada rule yang match                                  |
| `User Information`      | ✅ Yes    | Bisa kosong jika log tidak mencakup identitas user (e.g., network layer) |
| `Device Information`    | ✅ Yes    | Sama seperti di atas; tergantung log source                            |
| `Network Segment`       | ✅ Yes    | Bisa kosong jika tidak semua IP dimapping ke segmen                    |
| `Geo-location Data`     | ✅ Yes    | Tergantung ketersediaan hasil geolocation IP                           |
| `Proxy Information`     | ✅ Yes    | Hanya terisi jika traffic melalui proxy                                |
| `Firewall Logs`         | ✅ Yes    | Kosong jika log berasal dari selain firewall                           |
| `IDS/IPS Alerts`        | ✅ Yes    | Kosong jika tidak dari IDS/IPS atau tidak trigger rule                 |
| `Log Source`            | ✅ Yes    | Bisa kosong jika hanya dari satu source log (implisit)                 |

##### 4.2.Validity

Validitas setiap kolom dievaluasi dengan menetapkan aturan eksplisit, seperti:
	•	Format IP harus IPv4 yang valid dan tiap oktet bernilai 0–255
	•	Port berada di rentang 0–65535
	•	Timestamp sesuai standar waktu ISO
	•	Protocol dan Traffic Type mengikuti daftar yang disahkan

Selain itu, dilakukan validasi tambahan pada:
	•	IP address: terhadap layanan Realtime Blackhole List (RBL) untuk mendeteksi apakah IP termasuk daftar sumber serangan publik
	•	Device Information: mendeteksi user-agent yang sudah deprecated, seperti MSIE 5.0, yang sering diasosiasikan dengan aktivitas bot atau skrip otomatis.

Semua pelanggaran validitas ini direkam dalam laporan _records.csv, yang mencantumkan baris-baris bermasalah serta kolom yang menyebabkan kegagalan validasi (misalnya: Destination IP Address (RBL), Device Information (Suspect Bot)).

Dibawah ini adalah tabel yang kami jadikan rujukan untuk evaluasi validitas setiap kolom:

| Kolom                   | Valid? | Aturan Validitas                                                                                 |
|-------------------------|--------|---------------------------------------------------------------------------------------------------|
| `Timestamp`             | ✅     | Harus dalam format waktu valid (`YYYY-MM-DD HH:MM:SS`)                                            |
| `Source IP Address`     | ✅     | Harus berupa IP address IPv4 yang valid                                                           |
| `Destination IP Address`| ✅     | Harus berupa IP address IPv4 yang valid                                                           |
| `Source Port`           | ✅     | Angka 0–65535                                                                                      |
| `Destination Port`      | ✅     | Angka 0–65535                                                                                      |
| `Protocol`              | ✅     | Hanya salah satu dari: `TCP`, `UDP`, `ICMP`                                                       |
| `Packet Length`         | ✅     | Harus angka positif (> 0)                                                                         |
| `Packet Type`           | ✅     | Salah satu dari: `Data`, `Control`, `Ack`                                                         |
| `Traffic Type`          | ✅     | Harus termasuk: `HTTP`, `DNS`, `FTP`, `SSH`, `SMTP` (atau protokol standar lain)                 |
| `Attack Type`           | ✅     | Salah satu dari: `DoS`, `Brute Force`, `Phishing`, `SQL Injection`, `DDoS`, `Reconnaissance`, dll |
| `Attack Signature`      | ✅     | Harus string dengan pola penamaan signature yang dikenali                                         |
| `Action Taken`          | ✅     | Hanya salah satu dari: `Blocked`, `Allowed`, `Logged`, `Ignored`                                 |
| `Severity Level`        | ✅     | Harus: `Low`, `Medium`, `High`, atau `Critical`                                                   |
| `Payload Data`          | ⚠️     | Valid jika berupa teks atau null, tetapi bisa berisi konten tak relevan/noise                    |
| `Malware Indicators`    | ⚠️     | Harus salah satu dari: `None`, `Trojan`, `Worm`, `Ransomware`, `Spyware`, `IoC Detected`         |
| `Anomaly Scores`        | ✅     | Harus angka 0.0–100.0 (presentasi skala atau persen)                                              |
| `Alerts/Warnings`       | ⚠️     | Valid jika berupa string atau null; bisa noise jika tidak distandarisasi                         |
| `User Information`      | ⚠️     | Harus berupa string (nama), tetapi raw dan tidak terverifikasi                                   |
| `Device Information`    | ⚠️     | Harus berupa string (user agent/device ID)                                                       |
| `Network Segment`       | ⚠️     | Format bebas, tapi sebaiknya standar seperti `Segment A`, `Segment B`, dll.                      |
| `Geo-location Data`     | ⚠️     | Format seharusnya `City, Region`; valid jika bisa dipisah dua bagian                             |
| `Proxy Information`     | ⚠️     | Valid jika berisi IP, domain, atau tag proxy lain                                                |
| `Firewall Logs`         | ⚠️     | Valid jika string log; bisa noise jika tidak dibersihkan                                          |
| `IDS/IPS Alerts`        | ⚠️     | Valid jika berupa alert description; bisa beragam format                                         |
| `Log Source`            | ⚠️     | Valid jika berupa string sumber log (misal: `Firewall`, `Server`, `SIEM`)                        |

##### 4.3.Uniqueness

Beberapa kolom seperti Timestamp, Source IP Address, Destination IP Address, dan Attack Signature dapat dikombinasikan untuk membentuk entitas unik (deduplicated view). Meskipun tidak seluruh baris terduplikasi, kami menemukan sejumlah kejadian yang mirip secara timestamp dan pola signature — indikasi potensi flood attack atau logging burst akibat automated attack.

##### Candidate Key Combinations Used in Uniqueness Scoring

Berikut adalah kombinasi kolom yang digunakan untuk menilai keunikan (uniqueness) data:

| Kombinasi Kolom                                                      | Tujuan Penilaian Uniqueness                                                                      |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Timestamp + Source IP Address + Destination IP Address + Attack Signature | Mendeteksi apakah log serangan spesifik terjadi lebih dari sekali secara persis                 |
| Timestamp + Source IP Address + Destination Port                     | Mengungkap apakah sumber IP mengakses port target secara berulang pada waktu sama               |
| Source IP Address + Destination IP Address + Protocol + Attack Type  | Mengidentifikasi pola serangan yang konsisten dari IP tertentu                                   |
| Timestamp + Source IP Address + Protocol                             | Melihat kemungkinan flood/probing dari satu IP pada satu protokol dalam waktu sempit            |
| Attack Type + Destination Port                                       | Mengevaluasi apakah satu jenis serangan difokuskan pada port tertentu                            |
| Attack Signature + Severity Level                                    | Mencari tahu apakah signature yang sama muncul berulang dengan level severity yang identik       |

#### 5.Data Cleaning Strategy
##### 5.1.Ringkasan langkah pembersihan:
- Standarisasi
- Perbaikan/menghapus entri corrupt
- Normalisasi format (timestamp, IP, severity)
- Deduplication
##### 5.2.Justifikasi untuk setiap langkah (mengapa perlu dilakukan)

#### 6.Security Insight & Interpretation

##### 6.1.Anomaly Analysis
- Distribusi skor anomali
- Anomali yang tidak disertai alert (false negative?)
- Korelasi anomali dengan severity level & attack signature

##### 6.2.Pattern & Signature Analysis
Berdasarkan analisis pola kemunculan `Attack Signature` dalam jendela waktu sempit (1 hingga 10 menit), tidak ditemukan pola serangan signature yang berulang secara eksplisit dalam periode waktu tersebut. Dengan kata lain, tidak terdeteksi indikasi flood attack atau kampanye signature-based automated attack dalam dataset ini berdasarkan signature yang identik dalam waktu singkat.

Namun demikian, kami tetap mengevaluasi potensi aktivitas abnormal lainnya dengan pendekatan alternatif, seperti:
- IP source yang melakukan banyak serangan dalam waktu singkat
- Pola burst yang terindikasi dari kombinasi timestamp yang rapat

Analisis ini lebih cocok dikategorikan dalam evaluasi perilaku sumber serangan (source behavior analysis) ketimbang anomali berbasis duplikasi atau signature.

##### 6.3.Source Attribution
- IP atau lokasi geografis yang sering muncul sebagai sumber
- Perangkat/segmen jaringan yang paling sering menjadi target

##### 6.4.Temporal Trend
- **Flooding attack** atau **automated scan**
- Pengulangan serangan dari host/actor yang sama
- Aktivitas botnet atau skrip otomatis - Pola signature yang berulang tersebut tidak termasuk duplikasi data secara literal, namun mencerminkan pola kampanye serangan terkoordinasi atau noise akibat deteksi IDS yang agresif.

##### 6.5.Insider Threat / Lateral Movement Detection
- User/device yang menunjukkan perilaku abnormal

#### 7.Conclusion
- Kesimpulan temuan: status kualitas data, efektivitas deteksi ancaman, potensi risiko.
- Apa yang bisa diperbaiki dari sisi data & monitoring.

#### 8.Recommendations

Fokus pada dua area:
- Data Quality Improvement (e.g., sistem log harus enkripsi data penting, normalisasi field lebih awal).
- Security Monitoring & Detection (e.g., perlu fine-tuning IDS rule, tambahkan indikator GeoIP block).


#### 9.Appendix
- Dictionary kolom (glosarium).
- Log tambahan atau contoh deteksi.
- Skrip pembersihan data (jika disertakan).

##### Example SQL Queries for Pattern Analysis

Berikut ini adalah contoh query SQL yang digunakan dalam proses analisis pola serangan dan validasi anomali berdasarkan signature atau perilaku sumber serangan:

1. Query untuk mendeteksi signature yang muncul lebih dari 5 kali dalam 1 menit:
```sql
SELECT
    "Attack Signature",
    date_trunc('minute', CAST("Timestamp" AS TIMESTAMP)) AS minute_window,
    COUNT(*) AS occurrence
FROM cybersecurity_attacks_fixed
GROUP BY "Attack Signature", minute_window
HAVING COUNT(*) >= 5
ORDER BY occurrence DESC;
```

2. Query untuk mendeteksi serangan berulang dari satu IP dalam waktu singkat:
```sql
SELECT
    "Source IP Address",
    "Attack Signature",
    COUNT(*) AS total_hits,
    MIN(CAST("Timestamp" AS TIMESTAMP)) AS first_seen,
    MAX(CAST("Timestamp" AS TIMESTAMP)) AS last_seen
FROM cybersecurity_attacks_fixed
GROUP BY "Source IP Address", "Attack Signature"
HAVING COUNT(*) >= 10
ORDER BY total_hits DESC;
```

3. Query untuk mendeteksi burst aktivitas berdasarkan signature per 10 menit:
```sql
SELECT
    "Attack Signature",
    FLOOR(EXTRACT(epoch FROM CAST("Timestamp" AS TIMESTAMP)) / 600) AS time_bucket_10min,
    COUNT(*) AS count_per_10min
FROM cybersecurity_attacks_fixed
GROUP BY "Attack Signature", time_bucket_10min
HAVING COUNT(*) >= 8
ORDER BY count_per_10min DESC;
```