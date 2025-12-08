"""
Problem
-------
Given a list of VLANs and an expected VLAN range (e.g., 10–50),
find which VLANs are missing.

Concepts Practiced
------------------
- set difference
- range processing
- Useful in L2 automation & audits
"""

def missing_vlans(configured: list[int], start: int, end: int) -> list[int]:
    expected = set(range(start, end + 1))
    configured = set(configured)
    return sorted(expected - configured)


if __name__ == "__main__":
    print(missing_vlans([10, 12, 14, 20, 25], 10, 20))

