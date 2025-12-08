"""
Problem
-------
Extract all IPv4 addresses from arbitrary text/logs.

Concepts Practiced
------------------
- findall()
- Regex reuse
- Useful for parsing syslog, LLDP, traceroute, ACLs
"""

import re

ipv4 = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
ipv4_pattern = re.compile(rf'\b({ipv4}\.{ipv4}\.{ipv4}\.{ipv4})\b')

def extract_ips(text: str) -> list[str]:
    return ipv4_pattern.findall(text)


if __name__ == "__main__":
    sample = "Ping to 10.1.1.1 succeeded, backup 192.168.0.10 down."
    print(extract_ips(sample))

