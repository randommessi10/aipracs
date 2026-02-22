def dls(graph, node, target, limit, path, visited):
    path.append(node)
    visited.add(node)

    if node == target:
        print("Path:", path)
        return True

    if limit == 0:
        path.pop()
        visited.remove(node)
        return False

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, target, limit - 1, path, visited):
                return True

    path.pop()
    visited.remove(node)
    return False


def iddfs(graph, start, target, max_depth):
    for depth in range(max_depth + 1):
        path = []
        visited = set()
        if dls(graph, start, target, depth, path, visited):
            print("Target found at depth:", depth)
            return

    print("Target not found")

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

iddfs(graph, 'A', 'G', 3)
