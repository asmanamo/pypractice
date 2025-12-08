"""
Problem
-------
Parse Cisco 'show interface status' output.

Gi0/1   connected   a-full   a-1000   10/12
Te1/0   notconnect  auto     auto     1/5

Concepts Practiced
------------------
- Multi-space splitting
- Normalizing columns
"""

import re

def parse_int_status(lines: list[str]) -> list[dict]:
    results = []
    for line in lines:
        cols = re.split(r'\s{2,}', line.strip())
        if len(cols) >= 4:
            results.append({
                "interface": cols[0],
                "status": cols[1],
                "speed_duplex": cols[2],
                "vlan": cols[3]
            })
    return results


if __name__ == "__main__":
    sample = [
        "Gi0/1   connected   a-full   a-1000   10",
        "Te1/0   notconnect  auto     auto     1"

