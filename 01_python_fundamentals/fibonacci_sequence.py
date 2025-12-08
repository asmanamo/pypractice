"""
Problem
-------
Generate the first n numbers in the Fibonacci sequence.

Concepts Practiced
------------------
- List building in a loop
- Sequence logic and recurrence
- Returning values from functions
"""


def fibonacci(n: int) -> list[int]:
    """Return a list with the first n Fibonacci numbers starting from 0."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    # Already have 2 values; generate until length n
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    count = int(input("How many Fibonacci numbers do you want? "))
    print(fibonacci(count))

