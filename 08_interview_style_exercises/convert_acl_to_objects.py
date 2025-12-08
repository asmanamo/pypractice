"""
Problem
-------
Convert ACL entries into structured objects.

Why interviewers ask
--------------------
- Ability to parse semi-structured config
- Data modeling
"""

import re

pat = re.compile(
    r'permit\s+(?P<proto>\w+)\s+(?P<src>\S+)\s+(?P<dst>\S+)'
)

def parse_acl(lines):
    return [m.groupdict() for m in map(pat.match, lines) if m]


if __name__ == "__main__":
    acl = ["permit ip 10.1.1.0/24 192.168.0.0/24"]
    print(parse_acl(acl))

