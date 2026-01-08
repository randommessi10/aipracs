def astar(graph, start, goal, heuristic):
    openlist = {start}
    closed = set()
    parent = {start: None}
    g_cost = {start: 0}

    def f(node):
        return g_cost[node] + heuristic[node]

    while openlist:
        current = min(openlist, key=f)
        openlist.remove(current)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()

            print("Goal found:", goal)
            print("Path:", " -> ".join(path))
            print("Total cost:", g_cost[goal])
            return

        closed.add(current)

        for neighbour, cost in graph.get(current, []):
            new_g = g_cost[current] + cost

            if neighbour in closed:
                continue

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                parent[neighbour] = current
                openlist.add(neighbour)

    print("Goal not found")

graph = {
    'A': [('B', 1), ('C', 2), ('E', 2)],
    'B': [('D', 1), ('F', 5)],
    'C': [('E', 2)],
    'E': [('F', 2), ('D', 6)],
    'F': [('D', 1)],
    'D': []
}

heuristic_bad = {
    'A': 2,
    'B': 100,   # severely overestimated
    'C': 1,
    'E': 1,
    'F': 1,
    'D': 0
}

heuristic = {
    'A': 2,
    'B': 1,
    'C': 1,
    'E': 1,
    'F': 1,
    'D': 0
}

astar(graph, 'A', 'D', heuristic)
astar(graph, 'A', 'D', heuristic_bad)
