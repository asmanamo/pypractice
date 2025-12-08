"""
Problem
-------
Given a list of strings and a key, check whether the key is present.
If found, print the index; otherwise print 'not found'.

Concepts Practiced
------------------
- Iterating with range(len(list))
- Early return from functions
- Basic linear search
"""


def search_string(items: list[str], key: str) -> int:
    """
    Return the index of key in items if found, else -1.
    """
    for i in range(len(items)):
        if items[i] == key:
            return i
    return -1


if __name__ == "__main__":
    values = ["2", "55", "888", "9", "30", "45"]
    key = input("Enter key to search: ")

    index = search_string(values, key)
    if index == -1:
        print("Not found")
    else:
        print(f"{key} found at index {index}")

