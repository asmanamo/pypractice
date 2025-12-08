"""
Problem
-------
Use RESTCONF to fetch interface information from a network device.

Concepts Practiced
------------------
- HTTP Basic Auth
- RESTCONF headers
- JSON parsing
"""

import requests
import json

def restconf_get(interface: str):
    url = f"https://router1/restconf/data/ietf-interfaces:interfaces/interface={interface}"
    
    headers = {
        "Accept": "application/yang-data+json"
    }

    response = requests.get(url, headers=headers, auth=("admin", "admin"), verify=False)

    if response.status_code != 200:
        raise Exception(f"RESTCONF GET failed: {response.status_code}")

    return response.json()


if __name__ == "__main__":
    # Example only (no real device)
    print("RESTCONF call ready.")

