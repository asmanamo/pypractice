"""
Problem
-------
Given device inventory, detect IP overlaps.

Why interviewers ask
--------------------
- Ensuring uniqueness in automation
"""

def find_duplicates(ips):
    seen = set()
    dup = set()
    for ip in ips:
        if ip in seen:
            dup.add(ip)
        else:
            seen.add(ip)
    return sorted(dup)


if __name__ == "__main__":
    print(find_duplicates(["10.1.1.1","10.1.1.2","10.1.1.1"]))

