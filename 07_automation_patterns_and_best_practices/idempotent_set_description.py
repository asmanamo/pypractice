"""
Problem
-------
Implement idempotent interface description setter.

Concepts Practiced
------------------
- Idempotency (same input → same outcome)
- Pre-check before applying configuration
"""

def set_description(current_desc, desired_desc):
    """
    If the description already matches desired, do nothing.
    """
    if current_desc == desired_desc:
        return "no-change"
    else:
        return f"set desc to '{desired_desc}'"


if __name__ == "__main__":
    print(set_description("Uplink", "Uplink"))
    print(set_description("Old", "New-Uplink"))

