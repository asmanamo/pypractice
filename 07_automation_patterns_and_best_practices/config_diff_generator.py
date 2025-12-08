"""
Problem
-------
Return only the config lines that changed (diff logic).

Concepts Practiced
------------------
- Comparing configurations
- Producing minimal patch sets
"""

def diff_config(old: list[str], new: list[str]) -> dict:
    return {
        "to_add": [l for l in new if l not in old],
        "to_remove": [l for l in old if l not in new],
    }


if __name__ == "__main__":
    old = ["int Gi0/1", "desc A", "ip address 10.1.1.1 255.255.255.0"]
    new = ["int Gi0/1", "desc B", "ip address 10.1.1.1 255.255.255.0"]
    print(diff_config(old, new))

