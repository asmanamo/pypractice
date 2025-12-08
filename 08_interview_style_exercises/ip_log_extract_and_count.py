"""
Problem
-------
Given a device/syslog log, extract ALL IPv4 addresses and count
how many times they appear.

Why interviewers ask this
-------------------------
- Tests regex + counting (very common in telemetry/log parsing)
- Checks ability to sanitize input
"""

import re

ip = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
pattern = re.compile(rf'\b({ip}\.{ip}\.{ip}\.{ip})\b')

def extract_and_count(text: str) -> dict:
    ips = pattern.findall(text)
    freq = {}
    for ip in ips:
        freq[ip] = freq.get(ip, 0) + 1
    return freq


if __name__ == "__main__":
    sample = "Failed login from 10.1.1.1, then from 10.1.1.2 and 10.1.1.1 again"
    print(extract_and_count(sample))

