"""
Problem
-------
Given multiple route entries, pick the best based on:
1. Longest prefix
2. Lowest AD

Why interviewers ask
--------------------
- Routing logic
- Sorting + tuple keys
"""

def best_route(routes):
    return sorted(routes, key=lambda r: (-r["prefix"], r["ad"]))[0]


if __name__ == "__main__":
    data = [
        {"prefix": 24, "ad": 110, "nh": "1.1.1.1"},
        {"prefix": 16, "ad": 90, "nh": "2.2.2.2"},
        {"prefix": 24, "ad": 1, "nh": "3.3.3.3"},
    ]
    print(best_route(data))

