#!/usr/bin/python3
"""Find the minimum number of coins needed to make an amount."""


def makeChange(coins, total):
    """Return the fewest coins needed for total, or -1 if impossible."""
    if total <= 0:
        return 0

    denominations = sorted(set(coin for coin in coins
                               if 0 < coin <= total))
    if not denominations:
        return -1
    if total in denominations:
        return 1

    divisor = denominations[0]
    for coin in denominations[1:]:
        a, b = divisor, coin
        while b:
            a, b = b, a % b
        divisor = a

    if total % divisor:
        return -1
    if divisor != 1:
        total //= divisor
        denominations = [coin // divisor for coin in denominations]

    largest = denominations[-1]
    if total % largest == 0:
        return total // largest
    if len(denominations) == 1:
        return -1

    # For large totals, shortest paths by remainder avoid a huge DP table.
    # A coin c costs (largest - c) in the coin-count comparison.
    if total > 50000 and largest <= 10000:
        from heapq import heappop, heappush

        best = [None] * largest
        best[0] = (0, 0)
        queue = [(0, 0, 0)]
        target_remainder = total % largest
        while queue:
            penalty, value, remainder = heappop(queue)
            if best[remainder] != (penalty, value):
                continue
            if remainder == target_remainder and value <= total:
                return (total + penalty) // largest
            for coin in denominations[:-1]:
                next_remainder = (remainder + coin) % largest
                next_penalty = penalty + largest - coin
                next_value = value + coin
                candidate = (next_penalty, next_value)
                previous = best[next_remainder]
                if previous is None or candidate < previous:
                    best[next_remainder] = candidate
                    heappush(queue, (next_penalty, next_value,
                                     next_remainder))
        result = best[target_remainder]
        if result is not None and result[1] <= total:
            return (total + result[0]) // largest

    # Unbounded coin-change dynamic programming (exact for all coin sets).
    unreachable = total + 1
    minimum = [unreachable] * (total + 1)
    minimum[0] = 0
    for coin in denominations:
        for amount in range(coin, total + 1):
            candidate = minimum[amount - coin] + 1
            if candidate < minimum[amount]:
                minimum[amount] = candidate

    return -1 if minimum[total] == unreachable else minimum[total]
