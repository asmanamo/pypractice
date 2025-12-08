"""
Problem
-------
Extract BGP Large Communities: A:B:C

Concepts
--------
- RFC 8092
- Regex with 3 large integers
"""

import re

pattern = re.compile(r'(?P<comm>\d+:\d+:\d+)')

def extract_large_communities(text):
    return pattern.findall(text)


if __name__ == "__main__":
    s = "65000:100:1 65000:200:10 65100:5:20"
    print(extract_large_communities(s))

