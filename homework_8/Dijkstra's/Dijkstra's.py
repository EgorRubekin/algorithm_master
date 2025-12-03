def find_connected_components(graph):

    undirected = {v: set(neigh) for v, neigh in graph.items()}
    for v, neighs in graph.items():
        for u in neighs:
            if u not in undirected:
                undirected[u] = set()
            undirected[u].add(v)

    visited = set()
    components = []

    def dfs(start):
        stack = [start]
        comp = []
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                comp.append(v)
                stack.extend(undirected.get(v, []))
        return comp

    for vertex in undirected:
        if vertex not in visited:
            components.append(dfs(vertex))

    return components