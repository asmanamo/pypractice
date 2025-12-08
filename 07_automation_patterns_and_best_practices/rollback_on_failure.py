"""
Problem
-------
Simulate rollback if an operation fails.

Concepts Practiced
------------------
- Try/except
- Rollback blocks
"""

def apply_config(config):
    if "FAIL" in config:
        raise RuntimeError("Bad config")
    return "OK"

def transaction(config, rollback_config):
    try:
        return apply_config(config)
    except Exception:
        apply_config(rollback_config)
        return "rolled-back"


if __name__ == "__main__":
    print(transaction("desc FAIL", "desc previous"))

