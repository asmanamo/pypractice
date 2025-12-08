"""
Problem
-------
Given two lists list1 and list2, return elements that appear more often
in list1 than in list2 (respecting multiplicity).

Example:
    list1 = [2, 5, 5, 8, 8, 8, 9, 30, 45, 7, 7, 7]
    list2 = [4, 5, 5, 6, 7, 7, 8, 9, 10]
    -> [2, 8, 8, 8, 30, 45, 7, 7, 7]

Concepts Practiced
------------------
- list.count()
- Comparing frequencies between two containers
- Building a result list with conditions
"""


def list_minus(list1: list[int], list2: list[int]) -> list[int]:
    """Return list1 - list2 considering element counts."""
    result: list[int] = []
    for item in list1:
        if list1.count(item) > list2.count(item):
            result.append(item)
    return result


if __name__ == "__main__":
    l1 = [2, 5, 5, 8, 8, 8, 9, 30, 45, 7, 7, 7]
    l2 = [4, 5, 5, 6, 7, 7, 8, 9, 10]
    print(list_minus(l1, l2))

