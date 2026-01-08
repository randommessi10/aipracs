def dfs(graph, start):
    stack = []
    visited = {}

    stack.append(start)

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex, end=" ")
            visited[vertex] = True

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)


def bfs(graph, start):
    queue = []
    visited = {}

    queue.append(start)

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            print(vertex, end=" ")
            visited[vertex] = True

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
