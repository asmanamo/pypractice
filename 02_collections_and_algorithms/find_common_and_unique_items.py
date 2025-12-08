"""
Problem
-------
Given two lists (e.g., routes or IPs), find:
- common items
- unique to list1
- unique to list2

Concepts Practiced
------------------
- set operations
- Sorting output for readability
"""

def compare_lists(a: list[str], b: list[str]) -> dict:
    A, B = set(a), set(b)
    return {
        "common": sorted(A & B),
        "unique_to_a": sorted(A - B),
        "unique_to_b": sorted(B - A),
    }


if __name__ == "__main__":
    l1 = ["10.0.0.1", "10.0.0.2", "192.168.1.1"]
    l2 = ["10.0.0.2", "172.16.1.1"]

    print(compare_lists(l1, l2))

