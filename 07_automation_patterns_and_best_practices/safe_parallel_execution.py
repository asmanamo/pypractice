"""
Problem
-------
Run operations safely in parallel with per-task error handling.

Concepts Practiced
------------------
- try/except per thread
- result collection
"""

from concurrent.futures import ThreadPoolExecutor

def run_parallel(devices, function):
    results = {}
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(function, d): d for d in devices}
        for f, dev in futures.items():
            try:
                results[dev] = f.result()
            except Exception as e:
                results[dev] = f"error: {e}"
    return results


if __name__ == "__main__":
    def task(d):
        if d == "r2": raise Exception("boom")
        return "ok"

    print(run_parallel(["r1","r2","r3"], task))

