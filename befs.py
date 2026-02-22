def befs(graph, start, goal, heuristic):
    visited = {}
    queue = [(heuristic[start], start, [start])]

    while queue:
        queue.sort()   # lowest heuristic first
        cost, node, path = queue.pop(0)

        if node == goal:
            print("Goal found")
            print("Path:", path)
            return  # stop execution without returning the path

        if node not in visited:
            visited[node] = True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(
                        (heuristic[neighbor], neighbor, path + [neighbor])
                    )

    print("Goal not found")

# Example graph and heuristic
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 0
}

befs(graph, 'A', 'G', heuristic)
