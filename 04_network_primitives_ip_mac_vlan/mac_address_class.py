"""
Problem
-------
Represent a MAC address and normalize formats.

Concepts Practiced
------------------
- String cleanup
- Hex validation
- Reformatting
"""

import re

class MACAddress:
    pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$')

    def __init__(self, mac: str):
        mac = mac.strip().lower()
        if not self.pattern.fullmatch(mac):
            raise ValueError(f"Invalid MAC: {mac}")
        self.mac = mac.replace("-", ":")

    def normalized(self):
        return self.mac

    def as_int(self):
        return int(self.mac.replace(":", ""), 16)

    def __repr__(self):
        return f"MACAddress('{self.mac}')"


if __name__ == "__main__":
    print(MACAddress("AA-BB-CC-DD-EE-FF").as_int())

