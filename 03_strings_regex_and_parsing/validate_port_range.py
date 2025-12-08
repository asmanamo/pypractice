"""
Problem
-------
Validate port number: 0–65535.

Concepts Practiced
------------------
- Numeric regex range building
- Boundary checking without int conversion
"""

import re

port_pattern = re.compile(
    r'\b(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}|0)\b'
)

def validate_port(p: str) -> bool:
    return bool(port_pattern.fullmatch(p))


if __name__ == "__main__":
    tests = ["22", "443", "65535", "70000", "-1"]
    for t in tests:
        print(t, validate_port(t))

