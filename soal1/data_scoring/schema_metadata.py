columns_metadata = {
    "Timestamp": {
        "nullable": False,
        "validity": '"Timestamp" IS NOT NULL'
    },
    "Source IP Address": {
        "nullable": False,
        "validity": (
            'regexp_matches("Source IP Address", \'^(\\d+)\\.(\\d+)\\.(\\d+)\\.(\\d+)$\') IS NOT NULL AND '
            'try_cast(split_part("Source IP Address", \'.\', 1) AS INTEGER) BETWEEN 0 AND 255 AND '
            'try_cast(split_part("Source IP Address", \'.\', 2) AS INTEGER) BETWEEN 0 AND 255 AND '
            'try_cast(split_part("Source IP Address", \'.\', 3) AS INTEGER) BETWEEN 0 AND 255 AND '
            'try_cast(split_part("Source IP Address", \'.\', 4) AS INTEGER) BETWEEN 0 AND 255'
        )
    },
    "Destination IP Address": {
        "nullable": False,
        "validity": (
            'regexp_matches("Destination IP Address", \'^(\\d+)\\.(\\d+)\\.(\\d+)\\.(\\d+)$\') IS NOT NULL AND '
            'try_cast(split_part("Destination IP Address", \'.\', 1) AS INTEGER) BETWEEN 0 AND 255 AND '
            'try_cast(split_part("Destination IP Address", \'.\', 2) AS INTEGER) BETWEEN 0 AND 255 AND '
            'try_cast(split_part("Destination IP Address", \'.\', 3) AS INTEGER) BETWEEN 0 AND 255 AND '
            'try_cast(split_part("Destination IP Address", \'.\', 4) AS INTEGER) BETWEEN 0 AND 255'
        )
    },
    "Source Port": {"nullable": False, "validity": '"Source Port" BETWEEN 0 AND 65535'},
    "Destination Port": {"nullable": False, "validity": '"Destination Port" BETWEEN 0 AND 65535'},
    "Protocol": {"nullable": False, "validity": '"Protocol" IN (\'TCP\', \'UDP\', \'ICMP\')'},
    "Packet Length": {"nullable": False, "validity": '"Packet Length" > 0'},
    "Packet Type": {"nullable": False, "validity": '"Packet Type" IN (\'Data\', \'Control\', \'Ack\')'},
    "Traffic Type": {"nullable": False, "validity": '"Traffic Type" IN (\'HTTP\', \'DNS\', \'FTP\', \'SSH\', \'SMTP\')'},
    "Payload Data": {"nullable": True, "validity": 'TRUE'},
    "Malware Indicators": {"nullable": True, "validity": '"Malware Indicators" IN (\'None\', \'Trojan\', \'Worm\', \'Ransomware\', \'Spyware\', \'IoC Detected\')'},
    "Anomaly Scores": {"nullable": True, "validity": '"Anomaly Scores" BETWEEN 0 AND 100'},
    "Alerts/Warnings": {"nullable": True, "validity": 'TRUE'},
    "Attack Type": {"nullable": False, "validity": '"Attack Type" IN (\'DoS\', \'Brute Force\', \'Phishing\', \'SQL Injection\', \'DDoS\', \'Reconnaissance\', \'Malware\', \'Intrusion\')'},
    "Attack Signature": {"nullable": False, "validity": '"Attack Signature" IS NOT NULL'},
    "Action Taken": {"nullable": False, "validity": '"Action Taken" IN (\'Blocked\', \'Allowed\', \'Logged\', \'Ignored\')'},
    "Severity Level": {"nullable": False, "validity": '"Severity Level" IN (\'Low\', \'Medium\', \'High\', \'Critical\')'},
    "User Information": {"nullable": True, "validity": 'TRUE'},
    "Device Information": {
        "nullable": True,
        "validity": 'NOT regexp_matches("Device Information", \'.*MSIE 5\\.0.*\')'
    },
    "Network Segment": {"nullable": True, "validity": 'TRUE'},
    "Geo-location Data": {"nullable": True, "validity": 'regexp_matches("Geo-location Data", \'^[^,]+,\\s[^,]+$\') IS NOT NULL'},
    "Proxy Information": {"nullable": True, "validity": 'TRUE'},
    "Firewall Logs": {"nullable": True, "validity": 'TRUE'},
    "IDS/IPS Alerts": {"nullable": True, "validity": 'TRUE'},
    "Log Source": {"nullable": True, "validity": 'TRUE'}
}