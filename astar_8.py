# Manhattan distance heuristic
def heuristic(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            curr_row, curr_col = i // 3, i % 3
            goal_row, goal_col = goal_pos // 3, goal_pos % 3
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

# Get neighbors by moving blank tile
def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)
    row, col = zero_pos // 3, zero_pos % 3
    
    # up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))
    
    return neighbors

# Print state nicely
def print_puzzle(state):
    for i in range(3):
        print(state[i*3:(i+1)*3])

# A* Search
def a_star(start, goal):
    visited = []
    queue = [(heuristic(start, goal), 0, start, [start])]
    
    while queue:
        queue.sort()
        current = queue.pop(0)
        h = current[0]
        g = current[1]
        state = current[2]
        path = current[3]
        
        if state in visited:
            continue
        
        visited.append(state)
        
        if state == goal:
            print(f"Goal found! Total moves: {g}\n")
            print("Solution path:")
            for i, step in enumerate(path):
                print(f"\nMove {i}:")
                print_puzzle(step)
            return path
        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor, goal)
                new_path = path + [neighbor]
                queue.append((new_f, new_g, neighbor, new_path))
    
    return None

# Example: state as flat list [0-8]
start = (1, 2, 3, 4, 0, 5, 7, 8, 6)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

print("Start:", start)
print("Goal:", goal)
print("\nSolving...")
a_star(start, goal)