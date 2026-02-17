def waterjug(cap1,cap2,target):
    start = (0,0)
    queue = []
    queue.append((start,[]))
    visited = set()

    while queue:
        (jug1,jug2),path = queue.pop()
        if (jug1,jug2) in visited:
            continue
        visited.add((jug1,jug2))
        path = path + [(jug1,jug2)]
        if (jug1== target or jug2 == target):
            return path
        
        next_states = [
            (cap1,jug2),
            (jug1,cap2),
            (0,jug2),
            (jug1,0),
            (jug1-min(jug1,cap2-jug2),jug2+min(jug1,cap2-jug2)),
            (jug1+min(jug2,cap1-jug1),jug2-min(jug2,cap1-jug1))
        ]
        for state in next_states:
            if state not in visited:
                queue.append((state,path))
        
    return None

cap1 = int(input("Enter capacity of jug 1: "))
cap2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target: "))
solution = waterjug(cap1,cap2,target)
if solution:
    print("Path:")
    for state in solution:
        print(state)
else:
    print("No solution")