"""
Problem
-------
Sort a normal list AND sort a list of IP addresses correctly
(lexical sort breaks IP ordering).

Concepts Practiced
------------------
- sorted() vs list.sort()
- Custom sort keys
- Converting "x.y.z.w" -> tuple(int,int,int,int)
"""

def sort_ips(ip_list: list[str]) -> list[str]:
    return sorted(ip_list, key=lambda ip: tuple(map(int, ip.split("."))))


if __name__ == "__main__":
    numbers = [10, 3, 55, 1, 9]
    print("Sorted numbers:", sorted(numbers))

    ips = ["10.1.1.2", "192.168.1.1", "10.1.1.10", "10.1.1.3"]
    print("Lexical wrong:", sorted(ips))
    print("Correct IP sort:", sort_ips(ips))

