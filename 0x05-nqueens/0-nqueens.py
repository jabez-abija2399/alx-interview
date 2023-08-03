#!/usr/bin/python3
"""N Queens
n queens problem of placing n non-attacking queens on an n×n chessboard
solution requires that no two queens share the same row, column, or diagonal
"""
import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position (row, col)
    # without attacking any other queen on the board.
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(n):
    def backtrack(row):
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
