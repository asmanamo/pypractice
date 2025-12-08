"""
Problem
-------
Given a list of prefixes, check if any overlap (summarization / aggregation use case).

Concepts Practiced
------------------
- Binary mask conversion
- Range comparisons
- Sorting and interval overlap check
"""

def ip_to_int(ip: str) -> int:
    a, b, c, d = map(int, ip.split("."))
    return (a<<24) + (b<<16) + (c<<8) + d

def prefix_range(prefix: str) -> tuple[int, int]:
    ip, mask = prefix.split("/")
    mask = int(mask)
    base = ip_to_int(ip)
    size = 2**(32-mask)
    return (base, base + size - 1)

def find_overlaps(prefixes: list[str]) -> list[tuple[str, str]]:
    ranges = [(p, *prefix_range(p)) for p in prefixes]
    ranges.sort(key=lambda x: x[1])  # sort by base address

    overlaps = []
    for i in range(len(ranges) - 1):
        p1, s1, e1 = ranges[i]
        p2, s2, e2 = ranges[i+1]
        if e1 >= s2:
            overlaps.append((p1, p2))
    return overlaps


if __name__ == "__main__":
    pfx = ["10.1.1.0/24", "10.1.1.128/25", "10.2.0.0/16"]
    print(find_overlaps(pfx))

