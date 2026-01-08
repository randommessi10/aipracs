def befs(graph, start, goal, heuristic):
    visited = {}
    queue = [(heuristic[start], start)]
    while queue:
        queue.sort()
        cost, node = queue.pop(0)
        if node == goal:
            print("Goal found", node)
            return True
        if node not in visited:
            visited[node] = True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((heuristic[neighbor], neighbor))
    print("Goal not found")
    return False
