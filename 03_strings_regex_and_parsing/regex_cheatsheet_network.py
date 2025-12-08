"""
Collection of essential regex patterns for network automation.
Useful as a quick reference.

Patterns Included
-----------------
- IPv4
- IPv6
- MAC
- Port
- CIDR
"""

patterns = {
    "ipv4": r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b",
    "ipv6": r"\b(?:[A-Fa-f0-9]{1,4}:){1,7}[A-Fa-f0-9]{0,4}\b",
    "mac": r"\b([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b",
    "port": r"\b(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}|0)\b",
}

