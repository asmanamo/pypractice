"""
Problem
-------
Group IP addresses by their /24 subnet.

Network Use Case:
- Group users or devices per location
- Group DHCP leases
- Cluster logs by subnet

Concepts Practiced
------------------
- Dictionary grouping pattern
- String splitting
"""

def group_by_subnet(ips: list[str]) -> dict[str, list[str]]:
    groups = {}
    for ip in ips:
        subnet = ".".join(ip.split(".")[:3])  # /24 prefix
        groups.setdefault(subnet, []).append(ip)
    return groups


if __name__ == "__main__":
    sample_ips = [
        "10.1.1.5", "10.1.1.6", "10.1.2.1",
        "192.168.1.10", "192.168.1.20", "10.1.2.2"
    ]
    print(group_by_subnet(sample_ips))

