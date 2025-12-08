"""
Problem
-------
Parse LLDP neighbor info from raw text.

Example line:
LocalIntf   ChassisId       PortId       SysName
xe-0/0/1    b0:c6:9a:63:80   xe-3/2/0     sw-core01

Concepts Practiced
------------------
- Regex named groups
- Splitting + column parsing
"""

import re

pattern = re.compile(
    r'^(?P<local>\S+)\s+(?P<chassis>[0-9a-f:]+)\s+(?P<port>\S+)\s+(?P<sysname>\S+)$',
    re.IGNORECASE
)

def parse_lldp(lines: list[str]) -> list[dict]:
    results = []
    for line in lines:
        m = pattern.match(line.strip())
        if m:
            results.append(m.groupdict())
    return results


if __name__ == "__main__":
    data = [
        "xe-0/0/1    b0:c6:9a:63:80   xe-3/2/0     sw-core01",
        "xe-0/0/2    b0:c6:9a:63:81   xe-3/2/1     sw-edge01",
    ]
    print(parse_lldp(data))

