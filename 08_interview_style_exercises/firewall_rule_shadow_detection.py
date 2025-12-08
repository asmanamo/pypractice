"""
Problem
-------
Detect shadowed firewall rules:
Rule A is useless because rule B covers it.

Why interviewers ask
--------------------
- Understanding firewall logic
- Range & ordering reasoning
"""

def shadowed(rules):
    shadows = []
    for i in range(len(rules)-1):
        src1, dst1 = rules[i]
        for j in range(i+1, len(rules)):
            src2, dst2 = rules[j]
            if src2 in src1 and dst2 in dst1:
                shadows.append((rules[i], rules[j]))
    return shadows


if __name__ == "__main__":
    rules = [
        ("10.0.0.0/8", "ANY"),
        ("10.1.1.0/24", "ANY"),
    ]
    print(shadowed(rules))

