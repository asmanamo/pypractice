"""
Problem
-------
Validate an API response schema.

Concepts Practiced
------------------
- type checking
- schema enforcement without libraries
"""

def validate_schema(data: dict):
    required = {"hostname": str, "ip": str, "status": str}

    for key, t in required.items():
        if key not in data:
            return False
        if not isinstance(data[key], t):
            return False
    return True


if __name__ == "__main__":
    sample = {"hostname": "r1", "ip": "10.1.1.1", "status": "up"}
    print(validate_schema(sample))

