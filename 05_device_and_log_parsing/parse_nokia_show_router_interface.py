"""
Problem
-------
Parse Nokia SR-OS interface output.

Concepts
--------
- SR-OS format differences
- Key-value pairs
"""

import re

pattern = re.compile(
    r'Interface\s+(?P<intf>\S+).*?Address\s+(?P<ip>\d+\.\d+\.\d+\.\d+/\d+)',
    re.IGNORECASE
)

def parse_nokia(lines: list[str]):
    text = "\n".join(lines)
    return [m.groupdict() for m in pattern.finditer(text)]


if __name__ == "__main__":
    sample = [
        "Interface to-core-1",
        "  Admin Up, Oper Up",
        "  Address 10.1.1.1/24",
    ]
    print(parse_nokia(sample))

