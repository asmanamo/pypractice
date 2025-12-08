"""
Problem
-------
Common VLAN utilities:
- Check if valid
- Normalize list
- Expand "10,20-25,40"

Concepts Practiced
------------------
- Regex
- Range expansion
"""

import re

def is_valid_vlan(vlan: int) -> bool:
    return 1 <= vlan <= 4094

def expand_vlan_list(vlans: str) -> list[int]:
    result = []
    parts = vlans.split(",")
    for p in parts:
        if "-" in p:
            start, end = map(int, p.split("-"))
            result.extend(range(start, end+1))
        else:
            result.append(int(p))
    return [v for v in result if is_valid_vlan(v)]


if __name__ == "__main__":
    print(expand_vlan_list("10,20-22,4094,4095"))

