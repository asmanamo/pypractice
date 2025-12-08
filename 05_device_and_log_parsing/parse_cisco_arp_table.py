"""
Problem
-------
Parse Cisco ARP table:

Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.1.1.5               12   aabb.cc00.0101  ARPA   Gi0/1

Concepts Practiced
------------------
- Regex groups
- MAC normalization
- Device inventory building
"""

import re

arp_line = re.compile(
    r'^Internet\s+(?P<ip>\d+\.\d+\.\d+\.\d+)\s+\d+\s+(?P<mac>[\w\.]+)\s+\w+\s+(?P<intf>\S+)$'
)

def parse_arp(lines: list[str]) -> list[dict]:
    result = []
    for line in lines:
        m = arp_line.match(line.strip())
        if m:
            result.append(m.groupdict())
    return result


if __name__ == "__main__":
    sample = [
        "Internet  10.1.1.5  12  aabb.cc00.0101  ARPA  Gi0/1",
        "Internet  10.1.1.10  5   aabb.cc00.0202  ARPA  Gi0/2",
    ]
    print(parse_arp(sample))

