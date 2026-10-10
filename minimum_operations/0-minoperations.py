#!/usr/bin/python3
"""Calculate the minimum number of operations."""


def minOperations(n):
    """Return the minimum number of Copy All and Paste operations."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        operations += n

    return operations
