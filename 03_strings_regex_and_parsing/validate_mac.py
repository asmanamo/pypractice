"""
Problem
-------
Validate MAC address formats:
00:11:22:33:44:55
00-11-22-33-44-55

Concepts Practiced
------------------
- Character classes
- Repetition groups
"""

import re

mac_pattern = re.compile(
    r'\b([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b'
)

def validate_mac(mac: str) -> bool:
    return bool(mac_pattern.fullmatch(mac))


if __name__ == "__main__":
    tests = ["00:11:22:33:44:55", "AA-BB-CC-DD-EE-FF", "GG:11:22:33:44:55"]
    for t in tests:
        print(t, validate_mac(t))

