def analyze_dag(graph):

    visited = set()
    in_stack = set()
    parent = {}

    cycle_found = []

    def dfs(v):
        nonlocal cycle_found

        visited.add(v)
        in_stack.add(v)

        for u in graph.get(v, []):
            if u not in visited:
                parent[u] = v
                if dfs(u):
                    return True
            elif u in in_stack:
                cycle = [u]
                cur = v
                while cur != u:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(u)
                cycle_found = list(reversed(cycle))
                return True

        in_stack.remove(v)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return ("cycle", cycle_found)

    visited.clear()
    order = []

    def dfs2(v):
        visited.add(v)
        for u in graph.get(v, []):
            if u not in visited:
                dfs2(u)
        order.append(v)

    for node in graph:
        if node not in visited:
            dfs2(node)

    order.reverse()
    return ("toposort", order)
