"""
Problem
-------
Count occurrences of items using dictionary.

Network Use Case:
- Count ARP entries per VLAN
- Count interface flaps
- Count how many times an IP appears in logs

Concepts Practiced
------------------
- dict get(), increment pattern
- Clean counting loop
"""

def frequency_count(items: list[str]) -> dict[str, int]:
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


if __name__ == "__main__":
    logs = ["10.1.1.1", "10.1.1.2", "10.1.1.1", "10.1.1.3", "10.1.1.2", "10.1.1.1"]
    print(frequency_count(logs))

