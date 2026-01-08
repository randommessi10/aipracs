def befs(graph, start, goal, heuristic):
    visited = {}
    queue = [(heuristic[start], start, [start])]

    while queue:
        queue.sort()   # lowest heuristic first
        cost, node, path = queue.pop(0)

        if node == goal:
            print("Goal found")
            return path

        if node not in visited:
            visited[node] = True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(
                        (heuristic[neighbor], neighbor, path + [neighbor])
                    )

    print("Goal not found")
    return None
