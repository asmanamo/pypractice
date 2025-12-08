"""
Problem
-------
Given syslog entries with timestamps and interface names,
find interfaces that flapped more than N times in a window.

Why interviewers ask
--------------------
- Windowed counting
- Real-world automation use case
"""

import re

pat = re.compile(r'(?P<intf>Gi\d+/\d+)')

def find_flaps(log_lines: list[str], threshold: int) -> list[str]:
    counts = {}
    for line in log_lines:
        m = pat.search(line)
        if m:
            i = m.group("intf")
            counts[i] = counts.get(i, 0) + 1
    return [i for i, c in counts.items() if c >= threshold]


if __name__ == "__main__":
    logs = [
        "UPDOWN Gi0/1 up",
        "UPDOWN Gi0/1 down",
        "UPDOWN Gi0/1 up",
        "UPDOWN Gi0/2 up",
    ]
    print(find_flaps(logs, 2))

