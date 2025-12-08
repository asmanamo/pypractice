"""
Problem
-------
Generic syslog parser usable across Cisco/Juniper/Nokia/ASA.

Concepts
--------
- Regex multipliers
- Generalising timestamp formats
"""

import re

pattern = re.compile(
    r'^(?P<ts>\w+\s+\d+\s+\d+:\d+:\d+)\s+(?P<host>\S+)\s+(?P<msg>.*)$'
)

def parse_syslog(lines):
    return [m.groupdict() for m in map(pattern.match, lines) if m]


if __name__ == "__main__":
    sample = [
        "Jan 12 10:11:12 router1 %LINK-3-UPDOWN: Interface Gi0/1 up",
    ]
    print(parse_syslog(sample))

