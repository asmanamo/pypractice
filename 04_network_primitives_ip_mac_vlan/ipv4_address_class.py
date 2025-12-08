"""
Problem
-------
Create a class to represent an IPv4 address and validate it.

Concepts Practiced
------------------
- OOP for network primitives
- Validation logic
- Integer conversion
- IP comparisons
"""

class IPv4Address:
    def __init__(self, ip: str):
        self.ip = ip.strip()
        self.octets = self._validate(ip)

    def _validate(self, ip: str):
        parts = ip.split(".")
        if len(parts) != 4:
            raise ValueError(f"Invalid IPv4: {ip}")
        octets = []
        for p in parts:
            if not p.isdigit(): raise ValueError(f"Invalid: {p}")
            val = int(p)
            if not (0 <= val <= 255):
                raise ValueError(f"Octet out of range: {p}")
            octets.append(val)
        return octets

    def as_int(self):
        a,b,c,d = self.octets
        return (a<<24) + (b<<16) + (c<<8) + d

    def __lt__(self, other): return self.as_int() < other.as_int()
    def __eq__(self, other): return self.as_int() == other.as_int()

    def __repr__(self):
        return f"IPv4Address('{self.ip}')"


if __name__ == "__main__":
    print(IPv4Address("10.1.1.1"), IPv4Address("255.255.255.255").as_int())

