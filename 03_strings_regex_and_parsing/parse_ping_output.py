"""
Problem
-------
Parse a set of ping results:

[2025-11-12 10:01:23] PING 10.0.0.1: bytes=64 time=1.8 ms status=OK

Extract:
- IP
- time
- status

Concepts Practiced
------------------
- Regex extraction
- Dictionaries
"""

import re

pattern = re.compile(
    r'PING\s+(?P<ip>\d+\.\d+\.\d+\.\d+):.*?time=(?P<time>[0-9.]+).*?status=(?P<status>\w+)',
    re.IGNORECASE
)

def parse_ping(text: str) -> list[dict]:
    return [m.groupdict() for m in pattern.finditer(text)]


if __name__ == "__main__":
    log = """
    [2025] PING 10.0.0.1: bytes=64 time=1.8 ms status=OK
    PING 10.0.0.2: bytes=64 time=timeout status=FAIL
    """
    print(parse_ping(log))

