"""
Problem
-------
Convert an IP range (start,end) into minimum CIDR blocks.

Concepts Practiced
------------------
- Bit math
- Aggregation
- Useful for firewall policies in EU ISPs
"""

import ipaddress

def range_to_cidrs(start_ip: str, end_ip: str):
    start = int(ipaddress.IPv4Address(start_ip))
    end = int(ipaddress.IPv4Address(end_ip))
    nets = ipaddress.summarize_address_range(
        ipaddress.IPv4Address(start), ipaddress.IPv4Address(end)
    )
    return [str(n) for n in nets]


if __name__ == "__main__":
    print(range_to_cidrs("10.0.0.1", "10.0.0.50"))

