"""
Problem
-------
Make HTTPS GET to network monitoring API (Prometheus/Influx).

Concepts Practiced
------------------
- Basic GET
- JSON decode
"""

import requests

def get_metrics(url: str):
    resp = requests.get(url)
    return resp.status_code, resp.headers


if __name__ == "__main__":
    print("Metrics GET ready.")

