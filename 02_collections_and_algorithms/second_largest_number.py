"""
Problem
-------
Given a list of numbers, find the second largest distinct value.

Interview Classic.

Concepts Practiced
------------------
- set() to remove duplicates
- sorted() reverse
"""

def second_largest(nums: list[int]) -> int | None:
    unique = list(set(nums))
    if len(unique) < 2:
        return None
    return sorted(unique)[-2]


if __name__ == "__main__":
    print(second_largest([10, 5, 8, 8, 9]))

