# Making Change

A solution to the Holberton School interview project **Making Change**.

## Task 0: Change comes from within

The `makeChange(coins, total)` function finds the minimum number of coins
needed to make exactly `total`, with unlimited use of each denomination.
It returns `0` for a nonpositive total and `-1` when no solution exists.

The implementation is exact for arbitrary positive coin denominations. It
reduces denominations by their greatest common divisor, uses a remainder-
based optimization for large totals with modest denominations, and otherwise
uses unbounded coin-change dynamic programming.

## Example

```python
makeChange = __import__('0-making_change').makeChange
print(makeChange([1, 2, 25], 37))  # 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # -1
```
