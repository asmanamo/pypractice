"""
Problem
-------
You have two sets of devices. Find:
1. Devices in both lists (intersection)
2. Devices only in list A
3. Devices only in list B

Concepts Practiced
------------------
- set(), intersection, difference, union
- Very useful in network inventory comparison
"""

def compare_device_sets(a: list[str], b: list[str]):
    A, B = set(a), set(b)
    return {
        "common": A & B,
        "only_in_a": A - B,
        "only_in_b": B - A,
        "all_devices": A | B,
    }


if __name__ == "__main__":
    old = ["r1", "r2", "sw1", "fw1"]
    new = ["r2", "sw1", "sw2"]

    print(compare_device_sets(old, new))

