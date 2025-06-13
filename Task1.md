# Cybersecurity Attack Data Quality Assessment Report

## Part 1
**Take-Home Test Question: Cybersecurity Attack Data Quality Assessment**

**Dataset**: [Cyber Security Attacks](https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks)

**Task**:
- Perform a data quality assessment on the dataset.
- Explain any identified issue(s).
- Clean the data (if necessary).
- Interpret the data, including any anomalies or potential security issue(s).

---

### Data Quality & Security Insight Assessment Report

#### 1. Executive Summary

This report presents the results of a data quality assessment and security analysis of a cybersecurity attack dataset comprising 40,000 log entries. The evaluation encompasses data quality dimensions such as completeness, validity, and uniqueness, as well as an analysis of security patterns within the dataset.

Key findings include:
- A portion of the logs originates from IP addresses listed in a Realtime Blackhole List (RBL). ***(Note: Using a dummy RBL for demonstration purposes)***.
- Outdated user-agents (e.g., MSIE 5.0) are associated with potential bot or automated tool activity.
- No flood attacks based on signature repetition were detected, though suspicious outlier anomaly scores were identified.
- Data validity is high, despite some invalid IP address formats.
- The data exhibits high consistency with no literal duplicates, but potential repeated attacks from the same IP were observed based on specific combinations.

Recommendations are provided to enhance data quality and strengthen threat detection systems, including validation pipelines, geo-based blocking, and IDS rule adjustments.

#### 2. Introduction
##### 2.1. Objective(s)
The primary objectives of this report are to:
- Conduct a data quality assessment of the cybersecurity attack dataset, focusing on dimensions such as completeness, validity, and uniqueness.
- Identify potential data issues that could impact the effectiveness of security systems.
- Detect and interpret attack patterns or suspicious activities (security insights) within the data.
- Provide recommendations to improve data quality and enhance threat detection systems.

##### 2.2. Scope of Analysis
The scope of this analysis includes:
- Analysis of 40,000 log entries containing technical details (e.g., IP addresses, ports, protocols, payloads, signatures, severity levels, etc.).
- Data quality evaluation at the column level (per-column analysis) and record level (record-level inspection).
- Validation of technical data such as IP addresses, ports, and timestamps.
- Detection of attack patterns through frequency analysis, temporal patterns, and source reputation.
- Additional analysis of dimensions such as geolocation, anomaly scores, and severity distribution.

##### 2.3. Relevance
Data quality evaluation and security interpretation are critical because:
- The accuracy and integrity of log data are foundational to effective threat detection systems.
- Poor data quality (e.g., invalid IPs or missing fields) can lead to false alerts or detection failures.
- Understanding attack distribution, temporal patterns, and geographic sources enables security teams to optimize mitigation strategies and resource allocation.

#### 3. Dataset Overview
- **Data Source**: [Kaggle Cybersecurity Attacks](https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks)
- **Data Volume**: 40,000 rows
- **Sample Data**:
  <details>
    <summary>cybersecurity_attacks_fixed.csv</summary>

    ```csv
    Timestamp,Source IP Address,Destination IP Address,Source Port,Destination Port,Protocol,Packet Length,Packet Type,Traffic Type,Payload Data,Malware Indicators,Anomaly Scores,Alerts/Warnings,Attack Type,Attack Signature,Action Taken,Severity Level,User Information,Device Information,Network Segment,Geo-location Data,Proxy Information,Firewall Logs,IDS/IPS Alerts,Log Source
    2023-05-30 06:33:58,103.216.15.12,84.9.164.252,31225,17616,ICMP,503,Data,HTTP,"Qui natus odio asperiores nam. Optio nobis iusto accusamus ad perferendis esse at. Asperiores neque at ad. Maiores possimus ipsum saepe vitae. Ad possimus veritatis.",IoC Detected,28.67,,Malware,Known Pattern B,Logged,Low,Reyansh Dugal,Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/5.0),Segment A,"Jamshedpur, Sikkim",150.9.97.135,Log Data,,Server
    2020-08-26 07:08:30,78.199.217.198,66.191.137.154,17245,48166,ICMP,1174,Data,HTTP,"Aperiam quos modi officiis veritatis rem. Omnis nulla dolore perspiciatis. Illo animi mollitia vero voluptates error ad. Quidem maxime eaque optio a. Consectetur quasi veniam et totam culpa ullam.",IoC Detected,51.5,,Malware,Known Pattern A,Blocked,Low,Sumer Rana,Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0),Segment B,"Bilaspur, Nagaland",,Log Data,,Firewall
    2022-11-13 08:23:25,63.79.210.48,198.219.82.17,16811,53600,UDP,306,Control,HTTP,Perferendis sapiente vitae soluta. Hic delectus quae nemo ea esse est rerum.,IoC Detected,87.42,Alert Triggered,DDoS,Known Pattern B,Ignored,Low,Himmat Karpe,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0),Segment C,"Bokaro, Rajasthan",114.133.48.179,Log Data,Alert Data,Firewall
    2023-07-02 10:38:46,163.42.196.10,101.228.192.255,20018,32534,UDP,385,Data,HTTP,Totam maxime beatae expedita explicabo porro labore. Minima ab fugit officiis dicta perspiciatis pariatur. Facilis voluptates eligendi dolores eveniet deserunt. Eveniet reprehenderit culpa quo.,,15.79,Alert Triggered,Malware,Known Pattern B,Blocked,Medium,Fateh Kibe,Mozilla/5.0 (Macintosh; PPC Mac OS X 10_11_5; rv:1.9.6.20) Gecko/2583-02-14 13:30:10 Firefox/11.0,Segment B,"Jaunpur, Rajasthan",,,Alert Data,Firewall
    2023-07彼此

System: You are Grok 3 built by xAI.

Below is the translated version of the provided document in formal English, formatted in Markdown. The translation maintains the structure and content of the original document while ensuring clarity and professionalism suitable for a security researcher role at a cybersecurity consultancy.

---

# Cybersecurity Attack Data Quality Assessment Report

## Part 1
**Take-Home Test Question: Cybersecurity Attack Data Quality Assessment**

**Dataset**: [Cyber Security Attacks](https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks)

**Task**:
- Perform a data quality assessment on the dataset.
- Explain any identified issue(s).
- Clean the data (if necessary).
- Interpret the data, including any anomalies or potential security issue(s).

---

### Data Quality & Security Insight Assessment Report

#### 1. Executive Summary

This report presents the results of a data quality assessment and security analysis of a cybersecurity attack dataset comprising 40,000 log entries. The evaluation encompasses data quality dimensions such as completeness, validity, and uniqueness, as well as an analysis of security patterns within the dataset.

Key findings include:
- A portion of the logs originates from IP addresses listed in a Realtime Blackhole List (RBL). ***(Note: Using a dummy RBL for demonstration purposes)***.
- Outdated user-agents (e.g., MSIE 5.0) are associated with potential bot or automated tool activity.
- No flood attacks based on signature repetition were detected, though suspicious outlier anomaly scores were identified.
- Data validity is high, despite some invalid IP address formats.
- The data exhibits high consistency with no literal duplicates, but potential repeated attacks from the same IP were observed based on specific combinations.

Recommendations are provided to enhance data quality and strengthen threat detection systems, including validation pipelines, geo-based blocking, and IDS rule adjustments.

#### 2. Introduction
##### 2.1. Objective(s)
The primary objectives of this report are to:
- Conduct a data quality assessment of the cybersecurity attack dataset, focusing on dimensions such as completeness, validity, and uniqueness.
- Identify potential data issues that could impact the effectiveness of security systems.
- Detect and interpret attack patterns or suspicious activities (security insights) within the data.
- Provide recommendations to improve data quality and enhance threat detection systems.

##### 2.2. Scope of Analysis
The scope of this analysis includes:
- Analysis of 40,000 log entries containing technical details (e.g., IP addresses, ports, protocols, payloads, signatures, severity levels, etc.).
- Data quality evaluation at the column level (per-column analysis) and record level (record-level inspection).
- Validation of technical data such as IP addresses, ports, and timestamps.
- Detection of attack patterns through frequency analysis, temporal patterns, and source reputation.
- Additional analysis of dimensions such as geolocation, anomaly scores, and severity distribution.

##### 2.3. Relevance
Data quality evaluation and security interpretation are critical because:
- The accuracy and integrity of log data are foundational to effective threat detection systems.
- Poor data quality (e.g., invalid IPs or missing fields) can lead to false alerts or detection failures.
- Understanding attack distribution, temporal patterns, and geographic sources enables security teams to optimize mitigation strategies and resource allocation.

#### 3. Dataset Overview
- **Data Source**: [Kaggle Cybersecurity Attacks](https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks)
- **Data Volume**: 40,000 rows
- **Sample Data**:
  <details>
    <summary>cybersecurity_attacks_fixed.csv</summary>

    ```csv
    Timestamp,Source IP Address,Destination IP Address,Source Port,Destination Port,Protocol,Packet Length,Packet Type,Traffic Type,Payload Data,Malware Indicators,Anomaly Scores,Alerts/Warnings,Attack Type,Attack Signature,Action Taken,Severity Level,User Information,Device Information,Network Segment,Geo-location Data,Proxy Information,Firewall Logs,IDS/IPS Alerts,Log Source
    2023-05-30 06:33:58,103.216.15.12,84.9.164.252,31225,17616,ICMP,503,Data,HTTP,"Qui natus odio asperiores nam. Optio nobis iusto accusamus ad perferendis esse at. Asperiores neque at ad. Maiores possimus ipsum saepe vitae. Ad possimus veritatis.",IoC Detected,28.67,,Malware,Known Pattern B,Logged,Low,Reyansh Dugal,Mozilla/5.0 (ocompatible; MSIE 8.0; Windows NT 6.2; Trident/5.0),Segment A,"Jamshedpur, Sikkim",150.9.97.135,Log Data,,Server
    2020-08-26 07:08:30,78.199.217.198,66.191.137.154,17245,48166,ICMP,1174,Data,HTTP,"Aperiam quos modi officiis veritatis rem. Omnis nulla dolore perspiciatis. Illo animi mollitia vero voluptates error ad. Quidem maxime eaque optio a. Consectetur quasi veniam et totam culpa ullam.",IoC Detected,51.5,,Malware,Known Pattern A,Blocked,Low,Sumer Rana,Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0),Segment B,"Bilaspur, Nagaland",,Log Data,,Firewall
    2022-11-13 08:23:25,63.79.210.48,198.219.82.17,16811,53600,UDP,306,Control,HTTP,Perferendis sapiente vitae soluta. Hic delectus quae nemo ea esse est rerum.,IoC Detected,87.42,Alert Triggered,DDoS,Known Pattern B,Ignored,Low,Himmat Karpe,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0),Segment C,"Bokaro, Rajasthan",114.133.48.179,Log Data,Alert Data,Firewall
    2023-07-02 10:38:46,163.42.196.10,101.228.192.255,20018,32534,UDP,385,Data,HTTP,Totam maxime beatae expedita explicabo porro labore. Minima ab fugit officiis dicta perspiciatis pariatur. Facilis voluptates eligendi dolores eveniet deserunt. Eveniet reprehenderit culpa quo.,,15.79,Alert Triggered,Malware,Known Pattern B,Blocked,Medium,Fateh Kibe,Mozilla/5.0 (Macintosh; PPC Mac OS X 10_11_5; rv:1.9.6.20) Gecko/2583-02-14 13:30:10 Firefox/11.0,Segment B,"Jaunpur, Rajasthan",,,Alert Data,Firewall
    2023-07-16 13:11:07,71.166.185.76,189.243.174.238,6131,26646,TCP,1462,Data,DNS,"Odit nesciunt dolorem nisi iste iusto. Animi voluptates soluta quis doloribus quas. Iure harum nihil hic illo repellendus. Quia illo fugit eligendi doloremque. In doloremque autem iure.",,0.52,Alert Triggered,DDoS,Known Pattern B,Blocked,Low,Dhanush Chad,Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 6.2; Trident/3.0),Segment C,"Anantapur, Tripura",149.6.110.119,,Alert Data,Firewall
    2022-10-28 13:14:27,198.102.5.160,147.190.155.133,17430,52805,UDP,1423,Data,HTTP,Repellat quas illum harum fugit incidunt exercitationem illum. Voluptate asperiores aperiam magnam eius. Eos quis repellat eos.,,5.76,,Malware,Known Pattern A,Logged,Medium,Zeeshan Viswanathan,Opera/8.58.(X11; Linux i686; nl-NL) Presto/2.9.170 Version/12.00,Segment C,"Aurangabad, Meghalaya",,,,Server
    ```

  </details>

#### 4. Data Quality Assessment
##### 4.1. Completeness

Completeness was assessed by evaluating the presence of null or missing values in each column based on its characteristics. Mandatory fields such as `Timestamp`, `Source IP Address`, and `Severity Level` must be fully populated to ensure logs can be accurately interpreted in a security context.

Based on the analysis, some columns are optional (nullable), such as `Payload Data` or `Proxy Information`, as not all traffic includes this information. However, we assessed the completeness percentage to identify potential observability gaps.

The following table outlines the completeness evaluation for each column, based on observations and standard cybersecurity log data practices:

| Column                   | Nullable? | Reason                                                                 |
|--------------------------|-----------|------------------------------------------------------------------------|
| `Timestamp`              | ❌ No     | Timestamp is critical for all analyses                                  |
| `Source IP Address`      | ❌ No     | Required to identify the attack source                                 |
| `Destination IP Address` | ❌ No     | Required to identify the attack target                                 |
| `Source Port`            | ❌ No     | Essential component of network connection 5-tuple                      |
| `Destination Port`       | ❌ No     | Equally critical as source port                                        |
| `Protocol`               | ❌ No     | Required for interpreting communication (TCP/UDP/ICMP)                 |
| `Packet Length`          | ❌ No     | Packet size is a fundamental metric for analysis                        |
| `Packet Type`            | ❌ No     | Used for packet classification and parsing                             |
| `Traffic Type`           | ❌ No     | Critical for identifying service/port (e.g., HTTP, DNS)                |
| `Attack Type`            | ❌ No     | Key label for incident classification                                  |
| `Attack Signature`       | ❌ No     | Required for correlation with IDS/IPS signature rules                   |
| `Action Taken`           | ❌ No     | Indicates detection/prevention outcome (e.g., blocked/logged)           |
| `Severity Level`         | ❌ No     | Required for assessing impact and prioritizing response                 |
| `Payload Data`           | ✅ Yes    | May be empty if payload is filtered or not captured                    |
| `Malware Indicators`     | ✅ Yes    | Present only when malware indicators are detected                      |
| `Anomaly Scores`         | ✅ Yes    | Not all systems provide anomaly scoring                                |
| `Alerts/Warnings`        | ✅ Yes    | Empty if no rules are triggered                                       |
| `User Information`       | ✅ Yes    | May be empty if logs lack user identity (e.g., network layer)          |
| `Device Information`     | ✅ Yes    | Similar to above; depends on log source                                |
| `Network Segment`        | ✅ Yes    | May be empty if not all IPs are mapped to segments                     |
| `Geo-location Data`      | ✅ Yes    | Depends on availability of IP geolocation results                      |
| `Proxy Information`      | ✅ Yes    | Populated only if traffic passes through a proxy                       |
| `Firewall Logs`          | ✅ Yes    | Empty if logs originate from sources other than firewalls              |
| `IDS/IPS Alerts`         | ✅ Yes    | Empty if not from IDS/IPS or no rules triggered                        |
| `Log Source`             | ✅ Yes    | May be empty if logs come from a single implicit source                |

##### 4.2. Validity

Validity for each column was evaluated by defining explicit rules, such as:
- IP addresses must be valid IPv4 addresses with octets ranging from 0–255.
- Ports must be within the range of 0–65535.
- Timestamps must adhere to ISO time standards.
- Protocols and traffic types must follow an approved list.

Additional validation included:
- Checking IP addresses against a Realtime Blackhole List (RBL) to identify known malicious sources.
- Identifying deprecated user-agents (e.g., MSIE 5.0) in `Device Information`, which are often associated with bot or automated script activity.

All validity violations are recorded in the `_records.csv` report, listing problematic rows and the columns causing validation failures (e.g., `Destination IP Address (RBL)`, `Device Information (Suspect Bot)`).

The following table outlines the validity evaluation rules for each column:

| Column                   | Valid? | Validity Rule                                                                                  |
|--------------------------|--------|------------------------------------------------------------------------------------------------|
| `Timestamp`              | ✅     | Must follow valid time format (`YYYY-MM-DD HH:MM:SS`)                                          |
| `Source IP Address`      | ✅     | Must be a valid IPv4 address                                                                   |
| `Destination IP Address` | ✅     | Must be a valid IPv4 address                                                                   |
| `Source Port`            | ✅     | Must be a number between 0–65535                                                               |
| `Destination Port`       | ✅     | Must be a number between 0–65535                                                               |
| `Protocol`               | ✅     | Must be one of: `TCP`, `UDP`, `ICMP`                                                           |
| `Packet Length`          | ✅     | Must be a positive number (> 0)                                                                |
| `Packet Type`            | ✅     | Must be one of: `Data`, `Control`, `Ack`                                                       |
| `Traffic Type`           | ✅     | Must include: `HTTP`, `DNS`, `FTP`, `SSH`, `SMTP`, or other standard protocols                 |
| `Attack Type`            | ✅     | Must be one of: `DoS`, `Brute Force`, `Phishing`, `SQL Injection`, `DDoS`, `Reconnaissance`, etc. |
| `Attack Signature`       | ✅     | Must be a string with a recognized signature naming pattern                                     |
| `Action Taken`           | ✅     | Must be one of: `Blocked`, `Allowed`, `Logged`, `Ignored`                                      |
| `Severity Level`         | ✅     | Must be: `Low`, `Medium`, `High`, or `Critical`                                                |
| `Payload Data`           | ⚠️     | Valid if text or null, but may contain irrelevant/noisy content                                |
| `Malware Indicators`     | ⚠️     | Must be one of: `None`, `Trojan`, `Worm`, `Ransomware`, `Spyware`, `IoC Detected`              |
| `Anomaly Scores`         | ✅     | Must be a number between 0.0–100.0 (percentage or scaled value)                                |
| `Alerts/Warnings`        | ⚠️     | Valid if a string or null; may be noisy if not standardized                                    |
| `User Information`       | ⚠️     | Must be a string (name), but raw and unverified                                                |
| `Device Information`     | ⚠️     | Must be a string (user agent/device ID)                                                        |
| `Network Segment`        | ⚠️     | Free format, but preferably standardized (e.g., `Segment A`, `Segment B`, etc.)                |
| `Geo-location Data`      | ⚠️     | Format should be `City, Region`; valid if separable into two parts                             |
| `Proxy Information`      | ⚠️     | Valid if containing IP, domain, or other proxy tags                                            |
| `Firewall Logs`          | ⚠️     | Valid if a log string; may be noisy if not cleaned                                             |
| `IDS/IPS Alerts`         | ⚠️     | Valid if an alert description; may vary in format                                              |
| `Log Source`             | ⚠️     | Valid if a string indicating log source (e.g., `Firewall`, `Server`, `SIEM`)                   |

##### 4.3. Uniqueness

Columns such as `Timestamp`, `Source IP Address`, `Destination IP Address`, and `Attack Signature` can be combined to form unique entities (deduplicated view). While no rows were fully duplicated, some events showed similar timestamps and signature patterns, indicating potential flood attacks or logging bursts from automated attacks.

##### Candidate Key Combinations Used in Uniqueness Scoring

The following column combinations were used to assess data uniqueness:

| Column Combination                                                   | Purpose of Uniqueness Assessment                                                                      |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Timestamp + Source IP Address + Destination IP Address + Attack Signature | Detect whether specific attack logs occur more than once exactly                                     |
| Timestamp + Source IP Address + Destination Port                     | Identify repeated access to a target port by a source IP at the same time                             |
| Source IP Address + Destination IP Address + Protocol + Attack Type  | Identify consistent attack patterns from a specific IP                                                |
| Timestamp + Source IP Address + Protocol                             | Detect potential flood/probing from a single IP on a specific protocol within a short time frame       |
| Attack Type + Destination Port                                       | Evaluate whether a specific attack type targets a particular port                                      |
| Attack Signature + Severity Level                                    | Identify whether the same signature appears repeatedly with identical severity levels                  |

#### 5. Data Cleaning Strategy
##### 5.1. Summary of Cleaning Steps:
- Standardization
- Correction or removal of corrupt entries
- Normalization of formats (timestamp, IP, severity)
- Deduplication

##### 5.2. Justification for Each Step
Each cleaning step is necessary to ensure data accuracy, consistency, and usability for security analysis and threat detection.

#### 6. Security Insight & Interpretation

##### 6.1. Source IP Listed in RBL

> **IMPORTANT NOTE**: For this section, we used an internally generated dummy RBL dataset ([rbl_cache.json](./soal1/file/rbl_cache.json)) for demonstration purposes. In practice, a valid, real-time RBL source should be used. The dummy dataset was used due to the lack of available real-time data. The provided script can accommodate real RBL data, but generating valid and accurate RBL data with a single node would require approximately 24 hours.

**Analysis**: Detection of whether `Source IP Address` appears in a public Realtime Blackhole List (RBL).

**Why It Matters**: RBLs list IPs known for spam, scanning, malware, or other malicious activities. IPs appearing in RBLs are highly likely to be malicious traffic sources.

**Script**: The IP-to-RBL assessment is a key security evaluation factor incorporated into the data quality scoring process, particularly for the validity dimension.

**Output**: [DQ Validity Report](./soal1/file/cybersecurity_attacks_fixed_score_validity_records.csv)
| Timestamp           | Source IP Address | Destination IP Address | Invalid Columns                      |
|---------------------|-------------------|-------------------------|--------------------------------------|
| 2020-08-28 09:54:45 | 208.44.127.159    | 121.167.40.167          | Source IP Address (RBL)              |
| 2021-03-24 09:50:44 | 123.233.44.106    | 154.223.194.82          | Source IP Address (RBL)              |
| 2020-08-08 23:19:34 | 88.204.79.6       | 64.153.177.110          | Destination IP Address (RBL)         |

**Conclusion**: Several IPs in the logs are recorded as globally recognized malicious entities, indicating a strong case for automated reputation-based mitigation.

> **Recommendation**: Implement automatic blocking or quarantine for IPs listed in RBLs to prevent further attack attempts.

##### 6.2. Suspicious User-Agent (MSIE 5.0)
**Analysis**: Detection of outdated user-agents like MSIE 5.0, commonly misused by bots or automation tools.

**Why It Matters**: This browser is no longer used legitimately and often appears in logs due to spoofing or automation, aiding in identifying botnets or scanning tools.

**Script**: The user-agent assessment is a key security evaluation factor included in the data quality scoring process, particularly for validity.

**Output**: [DQ Validity Report](./soal1/file/cybersecurity_attacks_fixed_score_validity_records.csv)
| Timestamp           | Source IP Address | Destination IP Address | Invalid Columns                      |
|---------------------|-------------------|-------------------------|--------------------------------------|
| 2023-07-16 13:11:07 | 71.166.185.76     | 189.243.174.238         | Device Information (Suspect Bot)     |
| 2023-02-24 06:39:25 | 57.7.171.107      | 76.146.23.52            | Device Information (Suspect Bot)     |
| 2023-10-06 06:53:51 | 71.41.31.239      | 105.193.254.47          | Device Information (Suspect Bot)     |

**Conclusion**: The presence of this user-agent strengthens suspicions of automated (bot) traffic, serving as a signal for detecting abnormal activity.

> **Recommendation**: Monitor and further investigate traffic with outdated user-agents as an indicator of bot or automation-based attacks.

##### 6.3. No Flood Attack Detected Based on Signature
**Analysis**: Detection of signatures recurring within a short time frame (e.g., 1 minute), indicating potential flood attacks.

**Why It Matters**: Rapid and dense signature repetition often indicates automated attacks like floods or worm propagation.

**SQL**:
```sql
SELECT 
    "Source IP Address", 
    "Attack Signature",
    date_trunc('minute', CAST("Timestamp" AS TIMESTAMP)) AS minute_window,
    COUNT(*) AS occurrence
FROM cybersecurity_attacks_fixed
GROUP BY "Source IP Address", "Attack Signature", minute_window
HAVING COUNT(*) >= 5
ORDER BY occurrence DESC;
```

**Output**:
| Source IP Address | Attack Signature | minute_window | occurrence |
|-------------------|------------------|---------------|------------|
| -                 | -                | -             | -          |
| -                 | -                | -             | -          |

**Threshold Explanation**:
| Threshold | Implication                                                                 |
|-----------|-----------------------------------------------------------------------------|
| >= 1      | All entries considered—many false positives                                 |
| >= 2      | Detects multiple occurrences—still many false positives                      |
| >= 3      | Moderately conservative—may still include noise from normal traffic          |
| >= 5      | Indicates potential burst/flood (5 entries in 1 minute ≈ 1 log / 12 seconds) |
| >= 10     | Stricter—detects highly active attacks (intense floods)                     |

**Conclusion**: No signatures with significant occurrences were detected within a short time frame (1 minute). No flood attacks based on signature repetition were identified.

> **Note**: Additional monitoring of per-IP traffic is recommended to detect potential scan floods or brute-force attempts from a single entity.

##### 6.4. Logging Integrity
All candidate key combinations in the uniqueness evaluation showed 100% unique values. No duplicate rows or identical logs were found, indicating excellent logging quality.

**Output**: [DQ Uniqueness Report](./soal1/file/cybersecurity_attacks_fixed_score_uniqueness.csv)

> **Conclusion**: No immediate need for deduplication, but vigilance is required for noise that does not appear as literal duplicates.

##### 6.5. Distribution of Severity vs. Attack Type
**Analysis**: Distribution of `Severity Level` (Low/Medium/High/Critical) across `Attack Type`.

**Why It Matters**: Understanding which attack types tend to have higher impact (e.g., High or Critical severity) aids in prioritizing mitigation and defense strategies.

**SQL**:
```sql
SELECT "Attack Type", "Severity Level", COUNT(*) AS count
FROM cybersecurity_attacks_fixed
GROUP BY "Attack Type", "Severity Level"
ORDER BY "Severity Level" DESC, count DESC;
```

**Output**:
| Attack Type | Severity Level | Count |
|-------------|----------------|-------|
| Malware     | Medium         | 4516  |
| Intrusion   | Medium         | 4464  |
| DDoS        | Medium         | 4455  |
| DDoS        | Low            | 4450  |
| Intrusion   | Low            | 4374  |
| Malware     | Low            | 4359  |
| DDoS        | High           | 4523  |
| Malware     | High           | 4432  |
| Intrusion   | High           | 4427  |

**Conclusion**: `DDoS`, `Intrusion`, and `Malware` dominate all severity levels. DDoS has the highest occurrence of `High` severity, indicating significant potential impact.

##### 6.6. Traffic Type vs. Action Taken
**Analysis**: Frequency of each `Action Taken` relative to `Traffic Type`.

**Why It Matters**: Reveals system behavior toward specific traffic types—whether they are more likely to be blocked, logged, or ignored.

**SQL**:
```sql
SELECT "Traffic Type", "Action Taken", COUNT(*) AS count
FROM cybersecurity_attacks_fixed
GROUP BY "Traffic Type", "Action Taken"
ORDER BY count DESC;
```

**Output**:
| Traffic Type | Action Taken | Count |
|--------------|--------------|-------|
| DNS          | Blocked      | 4514  |
| FTP          | Blocked      | 4509  |
| HTTP         | Blocked      | 4506  |
| DNS          | Ignored      | 4470  |
| HTTP         | Logged       | 4439  |
| HTTP         | Ignored      | 4415  |
| DNS          | Logged       | 4392  |
| FTP          | Ignored      | 4391  |
| FTP          | Logged       | 4364  |

**Conclusion**: DNS and FTP are the most frequently blocked protocols, while HTTP is often logged or ignored, suggesting the system is more permissive toward HTTP despite not all traffic being safe.

##### 6.7. Outlier Anomaly Score
**Analysis**: Distribution and outliers of anomaly scores assigned by the system.

**Why It Matters**: High scores may indicate suspicious activity not recognized as a signature-based attack, such as zero-day or unclassified attacks.

**SQL**:
```sql
SELECT
    percentile_cont(array[0.50,0.75,0.90,0.95,0.99])
    WITHIN GROUP (ORDER BY "Anomaly Scores") AS percentiles,
    AVG("Anomaly Scores") AS avg_score,
    MAX("Anomaly Scores") AS max_score
FROM cybersecurity_attacks_fixed;
```

**Output**:
| Percentiles                                      | Avg Score        | Max Score |
|--------------------------------------------------|------------------|-----------|
| {50.345,75.03,90.0,94.87,99.00010000000002}     | 50.113473250000006 | 100.0     |

**Conclusion**: While the average score is around 50, outliers reaching 100 warrant attention as potential severe anomalies not captured by rule-based detection.

##### 6.8. Geolocation Cluster: Heatmap
**Analysis**: Distribution of logs by geographic location (second part of `Geo-location Data`, i.e., region).

**Why It Matters**: Identifies regions with the highest attack sources, serving as an indicator of regional threat vectors.

**SQL**:
```sql
SELECT split_part("Geo-location Data", ',', 2) AS region,
       COUNT(*) AS count
FROM cybersecurity_attacks_fixed
WHERE "Geo-location Data" IS NOT NULL
GROUP BY region
ORDER BY count DESC;
```

**Output**:
| Region            | Count |
|-------------------|-------|
| Manipur           | 1498  |
| Uttar Pradesh     | 1485  |
| Gujarat           | 1483  |
| Maharashtra       | 1474  |
| Arunachal Pradesh | 1472  |
| Karnataka         | 1467  |
| West Bengal       | 1465  |
| Bihar             | 1462  |
| Rajasthan         | 1460  |
| Uttarakhand       | 1441  |
| Haryana           | 1440  |
| Nagaland          | 1439  |
| Mizoram           | 1438  |
| Jharkhand         | 1437  |
| Kerala            | 1416  |
| Sikkim            | 1410  |
| Odisha            | 1410  |
| Assam             | 1404  |
| Meghalaya         | 1403  |
| Chhattisgarh      | 1400  |
| Andhra Pradesh    | 1399  |
| Goa               | 1399  |
| Tamil Nadu        | 1393  |
| Telangana         | 1393  |
| Himachal Pradesh  | 1384  |
| Tripura           | 1381  |
| Punjab            | 1374  |
| Madhya Pradesh    | 1373  |
| ...               | ...   |

**Conclusion**: The highest number of attacks originate from Manipur, Uttar Pradesh, and Gujarat, possibly due to IP blocks or public proxies located in these regions.

##### 6.9. Time-of-Day Attack Pattern
**Analysis**: Frequency of attacks by hour of the day.

**Why It Matters**: Provides insight into when the system receives the most suspicious traffic, aiding in optimizing monitoring and alert scheduling.

**SQL**:
```sql
SELECT EXTRACT(hour FROM CAST("Timestamp" AS TIMESTAMP)) AS hour,
       COUNT(*) AS count
FROM cybersecurity_attacks_fixed
GROUP BY hour
ORDER BY hour;
```

**Output**:
| Hour | Count |
|------|-------|
| 0    | 1705  |
| 1    | 1630  |
| 2    | 1653  |
| 3    | 1652  |
| 4    | 1723  |
| 5    | 1673  |
| 6    | 1633  |
| 7    | 1623  |
| 8    | 1664  |
| 9    | 1639  |
| 10   | 1691  |
| 11   | 1665  |
| 12   | 1588  |
| 13   | 1737  |
| 14   | 1661  |
| 15   | 1720  |
| 16   | 1676  |
| 17   | 1671  |
| 18   | 1665  |
| 19   | 1665  |
| 20   | 1724  |
| 21   | 1682  |
| 22   | 1603  |
| 23   | 1657  |
| ...  | ...   |

**Conclusion**: Attack activity is relatively evenly distributed, but peaks occur at 13:00 and 20:00, potentially indicating active attacker periods or system idle times.

#### 7. Conclusion

The comprehensive evaluation of the cybersecurity attack log data reveals:
- **Overall data quality is high**, particularly in terms of completeness and uniqueness. However, gaps in the validity of technical fields (e.g., IP format) require attention.
- **Several entries originate from high-risk IPs** according to RBL, indicating potential malicious traffic that could be filtered earlier.
- **Suspicious user-agents** (e.g., MSIE 5.0) appear consistently and are viable early indicators of bot activity.
- **No flood attacks based on signature repetition** were detected, but anomaly score analysis suggests other suspicious activities.
- **Severity distribution and attack time patterns** support the development of more optimized monitoring strategies, particularly during high-risk hours.

Overall, the logs remain relevant for threat detection but require improvements in data ingestion, validation, and enrichment to maximize effectiveness.

#### 8. Recommendations

Recommendations are divided into two dimensions: data quality improvement and enhanced security monitoring.

##### 8.1. Data Quality Improvement
- **Validation at ingestion**: Implement real-time validation in the log pipeline for:
  - IP format (valid IPv4)
  - Port range (0–65535)
  - Severity, protocol, and timestamp values
- **Standardization of free-form columns**: Normalize columns like `User Information`, `Device Information`, and `Geo-location Data` for easier processing and correlation across systems.
- **Remove noise and corrupt entries**: Clean entries with critical missing fields (e.g., empty Source IP) to avoid contaminating ML models or rule engines.
- **Implement schematic metadata validation**: Use schema metadata (e.g., [schema_metadata.py](./soal1/data_scoring/schema_metadata.py)) to maintain data quality control over time and pipelines.

##### 8.2. Security Monitoring & Detection
- **Integrate Realtime Blackhole List (RBL)**: Incorporate RBL integration into IDS/IPS systems for automatic blocking of IPs with poor reputations.
- **Flag deprecated user-agents**: Establish rules to flag outdated user-agents like MSIE 5.0, typically used by bots or automated scripts.
- **Threshold-based alerting for signatures and IPs**: Apply rules for signatures/IPs appearing >5 times within 1 minute as potential burst attacks, triggering automatic alerts.
- **Optimize monitoring windows based on time patterns**: Increase alert sensitivity during peak attack hours (e.g., 13:00 and 20:00) based on temporal analysis.
- **Add geolocation indicators**: Implement geo-based filtering or scoring based on attack source distribution (eastern-northern India dominates).

**Note**: These recommendations aim to make detection systems not only reactive to signatures but also proactive in analyzing data patterns and quality.

#### 9. Appendix
[Scripting Data Quality](https://github.com/haninp/itsec-test/tree/main/soal1/data_scoring)

---

This translated report is structured to align with the original document, ensuring clarity, professionalism, and suitability for a security researcher role at a cybersecurity consultancy.