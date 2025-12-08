"""
Problem
-------
Increment/decrement an IP address.

Concepts Practiced
------------------
- Integer conversion
"""

def increment_ip(ip: str):
    import ipaddress
    return str(ipaddress.IPv4Address(ip) + 1)

def decrement_ip(ip: str):
    import ipaddress
    return str(ipaddress.IPv4Address(ip) - 1)


if __name__ == "__main__":
    print(increment_ip("10.1.1.1"))
    print(decrement_ip("10.1.1.1"))

