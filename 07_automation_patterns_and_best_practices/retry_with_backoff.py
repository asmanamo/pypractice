"""
Problem
-------
Generic retry pattern with exponential backoff.

Concepts Practiced
------------------
- retries
- progressive delay
- error tolerance
"""

import time
import random

def retry(operation, retries=3, backoff=1):
    for attempt in range(retries):
        try:
            return operation()
        except Exception:
            time.sleep(backoff * (2 ** attempt))
    raise Exception("Operation failed after retries")


if __name__ == "__main__":
    # simulate flaky API
    def flaky():
        if random.random() < 0.7:
            raise Exception("API fail")
        return "success"

    print(retry(flaky))

