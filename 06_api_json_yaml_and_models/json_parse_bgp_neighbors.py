"""
Problem
-------
Given JSON from a controller (e.g., NSO, DNAC, Nokia NSP),
parse BGP neighbor status.

Concepts Practiced
------------------
- JSON traversal
- Conditional checks
"""

import json

def parse_bgp(json_data: dict):
    result = []
    for n in json_data.get("neighbors", []):
        result.append({
            "neighbor": n["addr"],
            "asn": n["asn"],
            "state": n["state"]
        })
    return result


if __name__ == "__main__":
    sample = {
        "neighbors": [
            {"addr": "10.0.0.1", "asn": 65000, "state": "up"},
            {"addr": "10.0.0.2", "asn": 65100, "state": "down"}
        ]
    }
    print(parse_bgp(sample))

