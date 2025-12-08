"""
Problem
-------
Given a list of (prefix, ASN) tuples, count how many prefixes each ASN announces.

Concepts Practiced
------------------
- Dict counting
- Grouping
- BGP table analysis pattern
"""

def count_routes(routes: list[tuple[str, int]]) -> dict[int, int]:
    counts = {}
    for prefix, asn in routes:
        counts[asn] = counts.get(asn, 0) + 1
    return counts


if __name__ == "__main__":
    data = [
        ("10.0.0.0/24", 65000),
        ("10.0.1.0/24", 65000),
        ("192.168.1.0/24", 65100),
    ]
    print(count_routes(data))

