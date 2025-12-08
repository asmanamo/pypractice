"""
Problem
-------
Load YAML safely.

Concepts
--------
- safe_load
- Avoid code execution vulnerabilities
"""

import yaml

def load_inventory(path):
    with open(path) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    print("Safe YAML loader ready.")

