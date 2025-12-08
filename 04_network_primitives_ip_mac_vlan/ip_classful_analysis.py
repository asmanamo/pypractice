"""
Problem
-------
Classify IPv4 into classful categories (A/B/C/D/E).

Concepts Practiced
------------------
- IP classification
"""

def classify_ip(ip):
    first = int(ip.split(".")[0])
    if 1 <= first <= 126: return "Class A"
    if 128 <= first <= 191: return "Class B"
    if 192 <= first <= 223: return "Class C"
    if 224 <= first <= 239: return "Class D (Multicast)"
    if 240 <= first <= 255: return "Class E (Experimental)"
    return "Invalid"


if __name__ == "__main__":
    print(classify_ip("10.1.1.1"))
    print(classify_ip("224.0.0.1"))

