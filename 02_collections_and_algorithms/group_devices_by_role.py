"""
Problem
-------
Given a list of (hostname, role), group by role:
routers, switches, firewalls, etc.

This appears frequently in EU automation interviews.

Concepts Practiced
------------------
- Dictionary grouping
- setdefault pattern
"""

def group_by_role(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}
    for host, role in entries:
        result.setdefault(role, []).append(host)
    return result


if __name__ == "__main__":
    devices = [
        ("r1", "router"),
        ("r2", "router"),
        ("sw1", "switch"),
        ("fw1", "firewall")
    ]
    print(group_by_role(devices))

