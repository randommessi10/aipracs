def a_star(graph, start, goal, heuristic):
    open_list = {start}
    closed_set = set()
    parent = {start: None}
    g_cost = {start: 0}

    def f(node):
        return g_cost[node] + heuristic[node]

    while open_list:
        current = min(open_list, key=f)
        open_list.remove(current)

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

        closed_set.add(current)

        for neighbour, cost in graph.get(current, []):
            new_g = g_cost[current] + cost

            if neighbour in closed_set:
                continue

            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                parent[neighbour] = current
                open_list.add(neighbour)

    print("Goal not found")
