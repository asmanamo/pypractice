"""
Problem
-------
Demonstrate good REST API error handling.

Concepts Practiced
------------------
- status code checks
- .json() errors
"""

import requests

def safe_get(url: str):
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        return {"error": "timeout"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}"}
    except ValueError:
        return {"error": "invalid JSON"}


if __name__ == "__main__":
    print("Safe GET ready.")

