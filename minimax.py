import math

def minimax(depth, node_index, is_max, values, alpha, beta):
    max_depth = int(math.log2(len(values)))
    # stop at leaf level
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = minimax(depth+1, node_index*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth+1, node_index*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

game_tree = [3,12,8,2,14,5,1,8]
result = minimax(0,0,True,game_tree,-math.inf,math.inf)
print(f"Optimal value using Minimax with alpha-beta pruning is {result}")
