"""
Problem
-------
Convert YAML file to JSON.

Concepts Practiced
------------------
- YAML parsing (Ansible-like format)
"""

import yaml
import json

def convert(yaml_file, json_file):
    data = yaml.safe_load(open(yaml_file))
    json.dump(data, open(json_file, "w"), indent=2)


if __name__ == "__main__":
    print("YAML ➜ JSON converter ready.")

