"""
Problem
-------
Check whether a given string is a palindrome (reads the same forward and backward).

Concepts Practiced
------------------
- String slicing
- Reversing strings using s[::-1]
- Case sensitivity and whitespace handling
"""


def is_palindrome(text: str, ignore_case: bool = True, strip_spaces: bool = True) -> bool:
    """Return True if text is a palindrome according to the chosen rules."""
    if strip_spaces:
        text = text.replace(" ", "")

    if ignore_case:
        text = text.lower()

    return text == text[::-1]


if __name__ == "__main__":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("Palindrome")
    else:
        print("Not a palindrome")

