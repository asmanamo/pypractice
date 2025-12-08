"""
Problem
-------
Generate and return the first n prime numbers.

Concepts Practiced
------------------
- While loop with dynamic termination
- Nested loop with early break
- Using previously found primes to speed up checks
"""


def first_n_primes(n: int) -> list[int]:
    if n <= 0:
        return []

    primes = [2]
    candidate = 3

    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2  # skip even numbers

    return primes


if __name__ == "__main__":
    n = int(input("Enter how many primes to generate: "))
    print(first_n_primes(n))

