"""
Problem
-------
Merge multiple device lists (from files, inventories, or APIs)
and produce a UNIQUE sorted inventory.

Concepts Practiced
------------------
- List merging
- Converting to set
- Sorting
"""

def merge_unique(*lists) -> list[str]:
    merged = set()
    for l in lists:
        merged.update(l)
    return sorted(merged)


if __name__ == "__main__":
    inv1 = ["r1", "r2", "r3"]
    inv2 = ["r2", "r4"]
    inv3 = ["sw1", "r3", "sw2"]

    print(merge_unique(inv1, inv2, inv3))

