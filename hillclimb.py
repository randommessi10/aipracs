import copy

# Goal state
GOAL = [[1,2,3],
        [4,0,5],
        [6,7,8]]

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Misplaced tiles heuristic
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL[i][j]:
                count += 1
    return count

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up down left right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

# Hill Climbing
def hill_climbing(start):
    current = start
    steps = 0

    while True:
        h = heuristic(current)

        print(f"Step {steps}  Heuristic={h}")
        for row in current:
            print(row)

        if current == GOAL:
            print("Goal State Reached!")
            return

        neighbors = get_neighbors(current)

        best = current
        best_h = h

        for n in neighbors:
            nh = heuristic(n)
            if nh < best_h:
                best = n
                best_h = nh

        if best_h >= h:
            print("Local optimum reached. Stopping.")
            return

        current = best
        steps += 1

# Example start state
start_state = [[2, 8, 3],
               [1, 6, 4],
               [7, 0, 5]]


hill_climbing(start_state)
