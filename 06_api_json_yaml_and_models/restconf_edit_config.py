"""
Problem
-------
Use RESTCONF to modify interface description.

Concepts Practiced
------------------
- PATCH vs PUT
- YANG JSON encoding
"""

import requests
import json

def restconf_set_description(intf: str, desc: str):
    url = f"https://router1/restconf/data/ietf-interfaces:interfaces/interface={intf}"

    payload = {
        "ietf-interfaces:interface": {
            "name": intf,
            "description": desc
        }
    }

    headers = {
        "Content-Type": "application/yang-data+json"
    }

    resp = requests.patch(url, headers=headers, json=payload,
                          auth=("admin", "admin"), verify=False)

    return resp.status_code


if __name__ == "__main__":
    print("PATCH ready for execution.")

