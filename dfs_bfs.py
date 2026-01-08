# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Depth-First Search (DFS) - Iterative using Stack
def dfs(graph, start):
    visited = {}
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            
            # Add neighbors in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited

# Breadth-First Search (BFS) using Queue
def bfs(graph, start):
    visited = {}
    queue = [start]
    visited.append(start)
    
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    
    return visited

print("DFS starting from 'A':")
dfs(graph, 'A')
print("\n")
print("BFS starting from 'A':")
bfs(graph, 'A')