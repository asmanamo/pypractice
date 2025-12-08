"""
Problem
-------
Parse OSPF neighbor states.

Example:
10.1.1.2      FULL/  -   00:11:22   Gig0/1

Concepts
--------
- Stateful protocols
- Extracting neighbor ID + interface
"""

import re

pattern = re.compile(
    r'^(?P<neighbor>\d+\.\d+\.\d+\.\d+)\s+(?P<state>\S+)/\S+\s+\S+\s+(?P<intf>\S+)$'
)

def parse_ospf(lines):
    return [m.groupdict() for m in map(pattern.match, lines) if m]


if __name__ == "__main__":
    lines = [
        "10.1.1.2 FULL/ - 00:11:22 Gi0/1"
    ]
    print(parse_ospf(lines))

