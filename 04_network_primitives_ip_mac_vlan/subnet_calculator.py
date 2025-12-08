"""
Problem
-------
Given an IP and mask, calculate:
- network address
- broadcast address
- number of hosts

Concepts Practiced
------------------
- Bitwise operations
- Subnet math
"""

def ip_to_int(ip):
    a,b,c,d = map(int, ip.split("."))
    return (a<<24)+(b<<16)+(c<<8)+d

def int_to_ip(n):
    return ".".join(str((n>>shift) & 255) for shift in [24,16,8,0])

def subnet_info(ip: str, prefix: int):
    base = ip_to_int(ip)
    mask = (0xffffffff << (32-prefix)) & 0xffffffff
    network = base & mask
    broadcast = network | (~mask & 0xffffffff)
    
    return {
        "network": int_to_ip(network),
        "broadcast": int_to_ip(broadcast),
        "hosts": max(0, broadcast - network - 1)
    }


if __name__ == "__main__":
    print(subnet_info("192.168.1.10", 24))

