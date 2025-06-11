import os
import json
import time
import ipaddress
import dns.resolver

RBL_PROVIDERS = [
    "zen.spamhaus.org",
    "bl.spamcop.net",
    "dnsbl.sorbs.net"
]

# Load cache dari file JSON
def load_cache(cache_path):
    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            return json.load(f)
    return {}

# Simpan cache ke file JSON
def save_cache(cache, cache_path):
    with open(cache_path, "w") as f:
        json.dump(cache, f, indent=2)

# Cek apakah IP ada di blacklist
def is_blacklisted(ip, cache):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.version != 4:
            return False

        now = time.time()

        # Gunakan cache jika belum kadaluarsa
        if ip in cache and (now - cache[ip].get("checked_at", 0)) < 86400:
            return cache[ip]["blacklisted"]

        reversed_ip = ".".join(reversed(ip.split(".")))
        for rbl in RBL_PROVIDERS:
            query = f"{reversed_ip}.{rbl}"
            try:
                dns.resolver.resolve(query, "A")
                # Jika resolve sukses → masuk blacklist
                cache[ip] = {"blacklisted": True, "checked_at": now}
                return True
            except dns.resolver.NXDOMAIN:
                continue
            except Exception:
                break  # Timeout atau error lain, anggap not listed

        cache[ip] = {"blacklisted": False, "checked_at": now}
        return False

    except Exception:
        return False