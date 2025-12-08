"""
Problem
-------
Run show commands on many devices concurrently.

Concepts
--------
- ThreadPoolExecutor
"""

from concurrent.futures import ThreadPoolExecutor

def run_commands(devices, cmd_fn):
    with ThreadPoolExecutor(max_workers=10) as pool:
        return list(pool.map(cmd_fn, devices))


if __name__ == "__main__":
    print(run_commands(["r1","r2"], lambda d: f"show version on {d}"))

