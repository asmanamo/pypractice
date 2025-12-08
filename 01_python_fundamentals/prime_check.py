"""
Problem
-------
Given an integer n, determine whether it is a prime number.

Concepts Practiced
------------------
- Input handling and type conversion (input -> int)
- Conditional logic
- for/else pattern in Python (else runs if loop wasn't broken)
- Basic number theory (divisibility test)
"""


def is_prime(number: int) -> bool:
    """Return True if number is prime, False otherwise."""
    if number <= 1:
        return False

    # No need to check beyond number // 2, but sqrt(number) is enough.
    # For interview readability, this version is simple:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Provide a number to check if it is prime: "))
    if is_prime(n):
        print("Prime number")
    else:
        print("Not a prime number")

