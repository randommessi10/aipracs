# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Iterative Deepening DFS
def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"Depth {depth}: ", end='')
        visited = []
        stack = [(start, 0)]
        
        while stack:
            node, current_depth = stack.pop()
            
            if node not in visited and current_depth <= depth:
                visited.append(node)
                print(node, end=' ')
                
                if current_depth < depth:
                    for neighbor in reversed(graph[node]):
                        if neighbor not in visited:
                            stack.append((neighbor, current_depth + 1))
        print()   
    return visited

print("IDDFS traversal from 'A' with max depth 3:")
iddfs(graph, 'A', 3)