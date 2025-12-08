"""
Problem
-------
Validate IPv6 addresses (supports compressed :: forms).

Concepts Practiced
------------------
- IPv6 structure
- Range matching
- Simplified practical regex
"""

import re

ipv6_pattern = re.compile(
    r'\b(?:[A-Fa-f0-9]{1,4}:){1,7}[A-Fa-f0-9]{0,4}\b'
)

def validate_ipv6(ip: str) -> bool:
    return bool(ipv6_pattern.fullmatch(ip))


if __name__ == "__main__":
    tests = ["2001:db8::1", "::1", "fe80::", "2001:::1"]
    for t in tests:
        print(t, validate_ipv6(t))

