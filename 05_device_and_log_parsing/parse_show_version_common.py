"""
Problem
-------
Parse show version from Cisco/Juniper/Arista to extract:
- model
- version
- uptime (if possible)

Concepts
--------
- Multi-vendor normalisation
"""

import re

cisco = re.compile(r'Cisco\s+(?P<model>\S+).*Version (?P<ver>[\w\.\(\)]+)')
juniper = re.compile(r'JUNOS Base OS boot \[(?P<ver>[\w\.]+)\]')
arista = re.compile(r'Arista\s+(?P<model>\S+).*Software image version (?P<ver>[\w\.]+)')

def parse_show_version(text):
    if m := cisco.search(text):
        return dict(type="cisco", model=m.group("model"), version=m.group("ver"))
    if m := juniper.search(text):
        return dict(type="juniper", version=m.group("ver"))
    if m := arista.search(text):
        return dict(type="arista", model=m.group("model"), version=m.group("ver"))
    return None


if __name__ == "__main__":
    print(parse_show_version("Cisco IOS-XE 4451-X Version 17.3.3"))
    print(parse_show_version("JUNOS Base OS boot [21.4R1]"))

