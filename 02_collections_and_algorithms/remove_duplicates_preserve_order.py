"""
Problem
-------
Remove duplicates from a list but KEEP the original order.

Network Use Case:
- Remove duplicate routes
- Clean IP lists coming from logs
- Remove duplicate syslog messages while keeping flow

Concepts Practiced
------------------
- set() tracking
- Order-preserving filtering
"""

def unique_preserve_order(items: list[str]) -> list[str]:
    seen = set()
    result = []
    for i in items:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


if __name__ == "__main__":
    data = ["r1", "r2", "r1", "r3", "r2", "r4"]
    print(unique_preserve_order(data))

