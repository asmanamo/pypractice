"""
Problem
-------
Convert JSON device inventory to YAML.

Concepts Practiced
------------------
- Serialization
- Data transformation
"""

import json
import yaml

def convert(json_file, yaml_file):
    data = json.load(open(json_file))
    yaml.dump(data, open(yaml_file, "w"), sort_keys=False)


if __name__ == "__main__":
    print("JSON ➜ YAML converter ready.")

