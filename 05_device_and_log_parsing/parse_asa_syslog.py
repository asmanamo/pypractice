"""
Problem
-------
Parse Cisco ASA syslog messages.

Example:
%ASA-4-313005: No matching connection for ICMP...

Concepts
--------
- Code extraction
- Severity parsing
"""

import re

pattern = re.compile(
    r'^%(?P<device>\w+)-(?P<severity>\d+)-(?P<code>\d+): (?P<msg>.*)$'
)

def parse_asa(lines):
    return [m.groupdict() for m in map(pattern.match, lines) if m]


if __name__ == "__main__":
    logs = [
        "%ASA-4-313005: No matching connection for ICMP",
        "%ASA-6-302013: Built outbound TCP connection"
    ]
    print(parse_asa(logs))

