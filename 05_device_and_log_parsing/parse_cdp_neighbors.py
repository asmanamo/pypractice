"""
Problem
-------
Parse Cisco CDP neighbors.

Device ID        Local Intf    Holdtime    Capability  Platform  Port ID
sw-core01        Gi0/1         153         S I         WS-C       Gi1/0/1

Concepts
--------
- Multi-column parsing
"""

import re

def parse_cdp(lines):
    results = []
    for l in lines:
        cols = re.split(r'\s{2,}', l.strip())
        if len(cols) >= 3 and "Gi" in cols[1]:
            results.append({
                "device": cols[0],
                "local": cols[1],
                "port": cols[-1]
            })
    return results


if __name__ == "__main__":
    d = ["sw-core01  Gi0/1 153 S I WS-C Gi1/0/1"]
    print(parse_cdp(d))

