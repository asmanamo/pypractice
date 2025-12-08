"""
Problem
-------
Create a simplified IPv6 representation with validation.

Concepts Practiced
------------------
- IPv6 structure
- Compression (::)
- Hex parsing
"""

import ipaddress

class IPv6Address:
    def __init__(self, ip: str):
        try:
            self.addr = ipaddress.IPv6Address(ip)
        except Exception as e:
            raise ValueError(f"Invalid IPv6: {ip}") from e

    def compressed(self):
        return self.addr.compressed

    def expanded(self):
        return self.addr.exploded

    def __repr__(self):
        return f"IPv6Address('{self.addr}')"


if __name__ == "__main__":
    print(IPv6Address("2001:db8::1").expanded())

