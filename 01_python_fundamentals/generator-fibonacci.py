def fibonacci_generator(max_count):
    """
    A generator function to calculate the Fibonacci sequence up to max_count.
    It yields each number instead of storing the entire sequence in memory.
    """
    a, b = 0, 1
    count = 0

    while count < max_count:
        yield a  # Yields the current number and pauses the function state
        a, b = b, a + b  # Calculates the next number pair
        count += 1

# --- Usage Example 1: Calculating the 500,000th number ---

# We only need the state of 'a' and 'b' at any given time, 
# not a list of 500,000 numbers.
# The sequence is calculated only as we iterate.
fib_gen = fibonacci_generator(500000)

# If we only want the 5th number:
import itertools
fifth_number = next(itertools.islice(fib_gen, 4, 5)) 

print(f"The 5th Fibonacci number is: {fifth_number}")
print(f"Type of fib_gen: {type(fib_gen)}")

# --- Usage Example 2: Iterating through a small subset ---
print("\nFirst 10 numbers:")
for number in fibonacci_generator(10):
    print(number, end=", ")
