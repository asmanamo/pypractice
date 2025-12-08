"""
Problem
-------
Given BGP AS-PATH strings, calculate path lengths.

Why interviewers ask
--------------------
- BGP fundamentals
- String parsing + counting
"""

def path_length(as_path: str) -> int:
    return len(as_path.split())


if __name__ == "__main__":
    print(path_length("65000 65100 65200"))
    print(path_length("65000"))

