def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                x,y = divmod(state[i][j]-1,3)
                h += abs(x-i) + abs(y-j)
    return h

def getNeighbour(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x,y = i,j
                dirs = [(-1,0),(1,0),(0,-1),(0,1)]
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0 <= nx < 3 and 0 <= ny < 3:
                        new = [list(r) for r in state]
                        new[x][y],new[nx][ny] = new[nx][ny],new[x][y]
                        moves.append(tuple(tuple(r) for r in new))
    return moves

def print_state(state):
    for row in state:
        print(row)
    print()

def astar_8puzzle(start):
    pq = [(heuristic(start), 0, start, [start])]
    visited = set()
    
    while pq:
        pq.sort()
        f, g, state, path = pq.pop(0)
        
        if state == goal:
            print(f"Solved in {len(path)-1} moves")
            print("Path to solution:")
            for i in range(len(path)):
                print(f"Step {i}:")
                print_state(path[i])
            return
        
        visited.add(state)
        
        for n in getNeighbour(state):
            if n not in visited:
                pq.append((g+1+heuristic(n), g+1, n, path + [n]))

start = ((1,2,3),(4,0,6),(7,5,8))
goal = ((1,2,3),(4,5,6),(7,8,0))
astar_8puzzle(start)