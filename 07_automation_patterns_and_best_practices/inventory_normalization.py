"""
Problem
-------
Normalize inconsistent inventory formats.

Concepts Practiced
------------------
- Data cleaning
- Key mapping
"""

def normalize_device(dev: dict) -> dict:
    return {
        "hostname": dev.get("host") or dev.get("name") or dev["hostname"],
        "mgmt_ip": dev.get("ip") or dev.get("mgmt_ip"),
        "vendor": dev.get("vendor", "").lower(),
    }


if __name__ == "__main__":
    d = {"host": "r1", "ip": "10.0.0.1", "vendor": "CISCO"}
    print(normalize_device(d))

