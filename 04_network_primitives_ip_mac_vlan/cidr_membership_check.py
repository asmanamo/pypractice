"""
Problem
-------
Check if an IP belongs to a CIDR block.

Concepts Practiced
------------------
- ipaddress module
"""

import ipaddress

def ip_in_cidr(ip: str, cidr: str) -> bool:
    return ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(cidr)


if __name__ == "__main__":
    print(ip_in_cidr("10.1.1.1", "10.1.0.0/16"))

