"""
Problem
-------
Parse Juniper “show interfaces terse”.

Concepts Practiced
------------------
- Split columns safely
- Extract admin/oper status
"""

import re

def parse_junos_terse(lines: list[str]) -> list[dict]:
    res = []
    for l in lines:
        cols = re.split(r'\s+', l.strip())
        if len(cols) >= 3 and "/" in cols[0]:
            res.append({
                "interface": cols[0],
                "admin": cols[1],
                "oper": cols[2]
            })
    return res


if __name__ == "__main__":
    data = [
        "ge-0/0/1 up up",
        "ge-0/0/2 down down"
    ]
    print(parse_junos_terse(data))

