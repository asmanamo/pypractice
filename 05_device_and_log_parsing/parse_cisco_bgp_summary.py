"""
Problem
-------
Parse Cisco BGP summary:

Neighbor        V    AS   MsgRcvd MsgSent  State/PfxRcd
10.0.0.1        4  65000     123     120        50

Concepts Practiced
------------------
- Column alignment parsing
- Numeric fields
"""

import re

bgp_pattern = re.compile(
    r'^(?P<neighbor>\d+\.\d+\.\d+\.\d+)\s+\d+\s+(?P<asn>\d+)\s+\d+\s+\d+\s+(?P<prefixes>\d+)$'
)

def parse_bgp(lines: list[str]):
    results = []
    for line in lines:
        m = bgp_pattern.match(line.strip())
        if m:
            results.append(m.groupdict())
    return results


if __name__ == "__main__":
    sample = [
        "10.0.0.1  4 65000 123 120 50",
        "10.0.0.2  4 65100 200 199 200"
    ]
    print(parse_bgp(sample))

