def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n, count):
    if row == n:
        count += 1
        print(f"Solution {count}")
        print_solution(board, n)
        return count

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            count = solve_n_queens(board, row + 1, n, count)
            board[row] = -1   # backtrack

    return count

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n = int(input("Enter N: "))
board = [-1] * n
total = solve_n_queens(board, 0, n, 0)

if total == 0:
    print("No solution")
