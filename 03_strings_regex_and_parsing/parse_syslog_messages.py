"""
Problem
-------
Extract timestamp, hostname, and message from syslog lines.

Concepts Practiced
------------------
- Regex with multiple groups
- Multi-field parsing
"""

import re

pattern = re.compile(
    r'^(?P<ts>\w+\s+\d+\s+\d+:\d+:\d+)\s+(?P<host>\S+)\s+(?P<msg>.*)$'
)

def parse_syslog(lines: list[str]) -> list[dict]:
    results = []
    for line in lines:
        m = pattern.match(line)
        if m:
            results.append(m.groupdict())
    return results


if __name__ == "__main__":
    logs = [
        "Jan 12 10:10:10 router1 %LINK-3-UPDOWN: Interface Gi0/1, changed state to up",
        "Jan 12 10:11:10 router1 %LINEPROTO-5-UPDOWN: Line protocol on Gi0/1 changed to down"
    ]
    print(parse_syslog(logs))

