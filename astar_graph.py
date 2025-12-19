# Graph representation with edge weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
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

# A* Search Algorithm
def a_star(graph, start, goal, heuristic):
    visited = []
    priority_queue = [(0 + heuristic[start], 0, start, [start])]
    
    while priority_queue:
        # Sort by f(n) = g(n) + h(n) and get node with lowest value
        priority_queue.sort()
        current = priority_queue.pop(0)
        f_cost = current[0]
        g_cost = current[1]
        node = current[2]
        path = current[3]
        
        if node in visited:
            continue
        
        visited.append(node)
        print(f"Visiting {node} (g={g_cost}, h={heuristic[node]}, f={f_cost})")
        
        if node == goal:
            print(f"\nGoal {goal} found!")
            print(f"Path: {' -> '.join(path)}")
            print(f"Total cost: {g_cost}")
            return path
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_g_cost = g_cost + weight
                new_f_cost = new_g_cost + heuristic[neighbor]
                new_path = path + [neighbor]
                priority_queue.append((new_f_cost, new_g_cost, neighbor, new_path))
    
    print(f"\nGoal {goal} not found!")
    return None

print("A* Search from 'A' to 'F':")
a_star(graph, 'A', 'F', heuristic)