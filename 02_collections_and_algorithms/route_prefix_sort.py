"""
Problem
-------
Given a list of route prefixes (IPv4 CIDR), sort them correctly by:
1. network address
2. prefix length

Common in EU interviews when handling:
- BGP table inspection
- Routing aggregation logic
- NSO/Ansible route templates

Concepts Practiced
------------------
- Custom key sorting
- Split IP into octets
- Extract prefix length
"""

def sort_prefixes(prefixes: list[str]) -> list[str]:
    def key_fn(p):
        ip, length = p.split("/")
        length = int(length)
        octs = tuple(map(int, ip.split(".")))
        return (octs, length)

    return sorted(prefixes, key=key_fn)


if __name__ == "__main__":
    data = ["10.1.1.0/24", "192.168.0.0/16", "10.1.0.0/16", "10.1.1.0/28"]
    print(sort_prefixes(data))

