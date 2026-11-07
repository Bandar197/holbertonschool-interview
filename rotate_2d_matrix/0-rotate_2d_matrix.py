#!/usr/bin/python3
"""Rotate a square matrix clockwise by 90 degrees in place."""


def rotate_2d_matrix(matrix):
    """Rotate the given square matrix clockwise without returning a value."""
    size = len(matrix)

    for row in range(size):
        for col in range(row + 1, size):
            matrix[row][col], matrix[col][row] = (
                matrix[col][row], matrix[row][col]
            )

    for row in matrix:
        row.reverse()
