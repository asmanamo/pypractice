"""
Problem
-------
Normalize IPs with mixed formatting:
- Leading zeros
- Extra spaces
- Random separators

Concepts Practiced
------------------
- Cleaning & normalizing input data
"""

def normalize_ip(ip: str) -> str:
    parts = ip.replace(" ", "").split(".")
    parts = [str(int(p)) for p in parts]  # removes leading zeros
    return ".".join(parts)


if __name__ == "__main__":
    tests = ["010.001.001.001", " 192 . 168 . 000 . 010 "]
    for t in tests:
        print(t, "->", normalize_ip(t))

