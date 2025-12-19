# Graph representation with heuristic values
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 0
}

# Best-First Search
def best_first_search(graph, start, goal, heuristic):
    visited = []
    priority_queue = [(heuristic[start], start)]
    
    while priority_queue:
        # Sort by heuristic value and get node with lowest heuristic
        priority_queue.sort()
        current = priority_queue.pop(0)
        node = current[1]
        
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            
            if node == goal:
                print(f"\nGoal {goal} found!")
                return visited
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    priority_queue.append((heuristic[neighbor], neighbor))
    
    print(f"\nGoal {goal} not found!")
    return visited

print("Best-First Search from 'A' to 'F':")
best_first_search(graph, 'A', 'F', heuristic)