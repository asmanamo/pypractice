"""
Problem
-------
Parse VLAN ranges like "10,20-25,30-32" → [10,20,21,22,23,24,25,30,31,32]

Why interviewers ask
--------------------
- Parsing, cleanup, and network basics
"""

def parse_vlan_range(vlans: str) -> list[int]:
    results = []
    for part in vlans.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            results.extend(range(start, end+1))
        else:
            results.append(int(part))
    return sorted(results)


if __name__ == "__main__":
    print(parse_vlan_range("10,20-22,100-102"))

