"""
Problem
-------
Consume an OpenAPI-defined service via Python.

Concepts Practiced
------------------
- Basic API client logic
- Endpoint abstraction
"""

import requests

class APIClient:
    def __init__(self, base):
        self.base = base

    def get_device(self, name):
        return requests.get(f"{self.base}/devices/{name}").json()


if __name__ == "__main__":
    print("OpenAPI client ready.")

