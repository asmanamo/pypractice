"""
Problem
-------
Validate IPv4 address using regex.

Concepts Practiced
------------------
- Regex grouping
- Boundary checks using numerical patterns
- Network-oriented input validation
"""

import re

ipv4_pattern = re.compile(
    r'\b('
    r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.'
    r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.'
    r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.'
    r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    r')\b'
)

def validate_ipv4(ip: str) -> bool:
    return bool(ipv4_pattern.fullmatch(ip))


if __name__ == "__main__":
    tests = ["10.1.1.1", "256.1.1.1", "192.168.0.500"]
    for t in tests:
        print(t, validate_ipv4(t))

