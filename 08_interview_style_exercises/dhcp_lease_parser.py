"""
Problem
-------
Parse simple DHCP lease entries.

Why interviewers ask
--------------------
- Basic text parsing
- IP extraction
"""

import re

pat = re.compile(r'^lease\s+(?P<ip>\d+\.\d+\.\d+\.\d+)\s+\{')

def parse_leases(lines):
    return [pat.match(l).group("ip") for l in lines if pat.match(l)]


if __name__ == "__main__":
    sample = ["lease 10.1.1.5 {", "lease 192.168.1.5 {"]

    print(parse_leases(sample))

