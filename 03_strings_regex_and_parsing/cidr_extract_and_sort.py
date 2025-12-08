"""
Problem
-------
Extract all CIDR prefixes from text and sort them.

Concepts Practiced
------------------
- Regex capture
- Sorting IP + prefix length
"""

import re

cidr_pattern = re.compile(
    r'\b((?:\d{1,3}\.){3}\d{1,3})/(3[0-2]|[12]?\d)\b'
)

def cidr_key(cidr: str):
    ip, length = cidr.split("/")
    octs = tuple(map(int, ip.split(".")))
    return (octs, int(length))

def extract_and_sort(text: str) -> list[str]:
    cidrs = cidr_pattern.findall(text)
    cidr_list = [f"{ip}/{mask}" for ip, mask in cidrs]
    return sorted(cidr_list, key=cidr_key)


if __name__ == "__main__":
    sample = "Routes: 10.1.1.0/24 192.168.0.0/16 10.1.0.0/16"
    print(extract_and_sort(sample))

