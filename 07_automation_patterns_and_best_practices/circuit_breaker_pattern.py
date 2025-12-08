"""
Problem
-------
Prevent overloading an API by introducing a circuit breaker.

Concepts
--------
- Failure thresholds
- Cooldown periods
"""

import time

class CircuitBreaker:
    def __init__(self, fail_limit=3, cooldown=10):
        self.fail_limit = fail_limit
        self.cooldown = cooldown
        self.fail_count = 0
        self.last_fail = 0

    def call(self, fn):
        if time.time() - self.last_fail < self.cooldown:
            raise Exception("Circuit open")

        try:
            result = fn()
            self.fail_count = 0
            return result
        except Exception:
            self.fail_count += 1
            self.last_fail = time.time()
            if self.fail_count >= self.fail_limit:
                raise Exception("Circuit open")
            raise


if __name__ == "__main__":
    cb = CircuitBreaker()
    print("Circuit breaker ready.")

