"""
Problem
-------
Convert netmask <-> prefix length.

Concepts Practiced
------------------
- Bit counting
"""

def mask_to_prefix(mask: str) -> int:
    bits = "".join(f"{int(octet):08b}" for octet in mask.split("."))
    return bits.count("1")

def prefix_to_mask(prefix: int) -> str:
    mask = (0xffffffff << (32-prefix)) & 0xffffffff
    return ".".join(str((mask >> i) & 255) for i in [24,16,8,0])


if __name__ == "__main__":
    print(mask_to_prefix("255.255.255.0"))
    print(prefix_to_mask(24))

