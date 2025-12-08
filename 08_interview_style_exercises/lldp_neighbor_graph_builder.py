"""
Problem
-------
Build a network graph from LLDP neighbors.

Why interviewers ask this
-------------------------
- Tests understanding of topology relationships
- Ability to dedupe edges and represent as adjacency list
"""

def build_graph(neighbors):
    graph = {}
    for local, remote in neighbors:
        graph.setdefault(local, set()).add(remote)
        graph.setdefault(remote, set()).add(local)
    return {k: sorted(v) for k, v in graph.items()}


if __name__ == "__main__":
    lldp = [("r1","sw1"),("sw1","r2"),("r2","sw2"),("sw1","r1")]
    print(build_graph(lldp))

