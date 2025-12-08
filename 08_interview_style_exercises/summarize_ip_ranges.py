"""
Problem
-------
Given a list of IP ranges, summarize into minimal CIDRs.

Why interviewers ask
--------------------
- Subnetting knowledge
- Ability to use 'ipaddress' module
"""

import ipaddress

def summarize_ranges(ranges):
    cidrs = []
    for start, end in ranges:
        nets = ipaddress.summarize_address_range(
            ipaddress.IPv4Address(start), ipaddress.IPv4Address(end)
        )
        cidrs.extend(str(n) for n in nets)
    return cidrs


if __name__ == "__main__":
    print(summarize_ranges([("10.0.0.1","10.0.0.20")]))

