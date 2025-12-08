"""
Problem
-------
LLDP neighbours may be seen twice (A->B and B->A).  
Given LLDP edges, return UNIQUE links.

Concept Practiced
------------------
- Sets of frozensets
- Deduping unordered pairs (A-B == B-A)
- Network topology normalization
"""

def unique_links(neighbors: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen = set()
    for a, b in neighbors:
        seen.add(frozenset({a, b}))
    return [tuple(sorted(pair)) for pair in seen]


if __name__ == "__main__":
    lldp = [
        ("r1", "sw1"),
        ("sw1", "r1"),
        ("r2", "sw1"),
        ("sw1", "r2")
    ]
    print(unique_links(lldp))

