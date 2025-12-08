"""
Problem
-------
Given a list of interface flap events, detect interfaces with flaps > threshold.

Concepts Practiced
------------------
- Counting (dict)
- Filtering based on frequency
- Real-life EU interview scenario (BT, Vodafone, Nokia)
"""

def detect_flaps(events: list[str], threshold: int) -> list[str]:
    counts = {}
    for intf in events:
        counts[intf] = counts.get(intf, 0) + 1
    return [i for i, c in counts.items() if c > threshold]


if __name__ == "__main__":
    events = ["Gi0/1", "Gi0/1", "Gi0/2", "Gi0/1", "Gi0/3", "Gi0/3"]
    print(detect_flaps(events, threshold=2))

