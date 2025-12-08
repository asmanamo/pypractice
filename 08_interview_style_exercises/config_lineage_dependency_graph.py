"""
Problem
-------
Given "interface depends on vlan" or "ospf depends on loopback",
build a dependency tree.

Why interviewers ask
--------------------
- Understanding hierarchical configs
- Graph relationships
"""

def build_dependency_graph(pairs):
    graph = {}
    for parent, child in pairs:
        graph.setdefault(parent, []).append(child)
    return graph


if __name__ == "__main__":
    deps = [("ospf","lo0"),("ospf","vlan10"),("vlan10","Gi0/1")]
    print(build_dependency_graph(deps))

