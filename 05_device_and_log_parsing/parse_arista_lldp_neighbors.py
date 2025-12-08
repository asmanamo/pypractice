"""
Problem
-------
Parse Arista EOS LLDP neighbors.

Port       Neighbor Device   Neighbor Port
Et1        sw-core01         Et49/1

Concepts
--------
- Multi-space separation
"""

import re

def parse_arista_lldp(lines: list[str]):
    res = []
    for l in lines:
        cols = re.split(r'\s{2,}', l.strip())
        if len(cols) == 3 and cols[0].startswith("Et"):
            res.append({
                "local": cols[0],
                "neighbor": cols[1],
                "neighbor_port": cols[2]
            })
    return res


if __name__ == "__main__":
    data = ["Et1    sw-core01    Et49/1"]
    print(parse_arista_lldp(data))

