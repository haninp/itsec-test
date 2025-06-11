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
### 4.1 Completeness

Berikut ini adalah penilaian kelengkapan (completeness) kolom berdasarkan hasil observasi dan praktik umum dalam log data cybersecurity:

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

##### 4.2.Uniqueness
##### 4.3.Validity

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
- Attack signature paling sering muncul
- Tipe serangan dominan (e.g., scanning, malware, brute force)

##### 6.3.Source Attribution
- IP atau lokasi geografis yang sering muncul sebagai sumber
- Perangkat/segmen jaringan yang paling sering menjadi target

##### 6.4.Temporal Trend
- Waktu puncak serangan
- Adakah indikasi campaign terkoordinasi?

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