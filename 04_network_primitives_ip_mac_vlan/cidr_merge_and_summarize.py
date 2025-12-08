"""
Problem
-------
Summarize a list of CIDRs (merge overlapping networks).

Concepts Practiced
------------------
- IP summarization
- ipaddress module
"""

import ipaddress

def summarize(prefixes: list[str]):
    nets = [ipaddress.IPv4Network(p) for p in prefixes]
    return [str(n) for n in ipaddress.collapse_addresses(nets)]


if __name__ == "__main__":
    print(summarize(["10.0.0.0/24", "10.0.1.0/24", "10.0.0.0/25"]))

