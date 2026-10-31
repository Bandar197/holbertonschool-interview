#!/usr/bin/python3
"""Solve the N Queens puzzle using backtracking."""

import sys


def is_safe(queens, column):
    """Check whether a queen can be placed safely."""
    row = len(queens)

    for previous_row, previous_column in enumerate(queens):
        if previous_column == column:
            return False

        if abs(previous_column - column) == row - previous_row:
            return False

    return True


def solve_nqueens(n, queens):
    """Find and print all valid N Queens solutions."""
    row = len(queens)

    if row == n:
        solution = [
            [index, column]
            for index, column in enumerate(queens)
        ]
        print(solution)
        return

    for column in range(n):
        if is_safe(queens, column):
            queens.append(column)
            solve_nqueens(n, queens)
            queens.pop()


def main():
    """Validate arguments and solve the N Queens puzzle."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n, [])


if __name__ == "__main__":
    main()
