# N Queens

This project solves the N Queens puzzle using Python
and the backtracking algorithm.

## Requirements

- Python 3.4.3
- PEP 8 style
- Only the sys module is allowed

## Usage

```bash
./0-nqueens.py N
```

N must be an integer greater than or equal to 4.

## Algorithm

The program uses recursive backtracking to place
queens on an N x N chessboard.

Each queen must be placed in a different row
and column without attacking another queen
diagonally.

The program prints every valid solution.

## Examples

```bash
./0-nqueens.py 4
./0-nqueens.py 6
```
