"""
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.

Coin Change Problem
"""

from math import inf


def coin_change_bottom_up(coins, N):
    memo = [inf] * (N + 1)
    memo[0] = 0
    for value in range(1, N + 1):
        for j in range(len(coins)):  # go through coins
            if coins[j] <= value:
                balance = value - coins[j]
                count = 1 + memo[balance]
                if count < memo[value]:  # if there's new optimal
                    memo[value] = count
    return memo[N]


def coin_change_top_down(coins, value):
    memo = [-1] * len(coins)
    memo[0] = 0
    if memo[value] != -1:  # infinity is incorrect
        return memo[value]
    else:
        minCoins = inf
        for i in range(1, len(coins)):
            if coins[i] <= value:
                c = 1 + coin_change_top_down(value - coins[i])
                if c < minCoins:
                    minCoins = c
        memo[value] = minCoins
        return memo[value]


def min_coins(coins, V):
    coins_required = [inf] * (V + 1)
    coins_required[0] = 0

    for i in range(1, V + 1):
        if i >= min(coins):
            best_so_far = inf
            for c in coins:
                if c <= i:
                    best_so_far = min(best_so_far, 1 + coins_required[i - c])
            coins_required[i] = best_so_far
    print(coins_required)
    return coins_required[V]


coins = [9, 5, 6, 1]
print(min_coins(coins, 12))


def min_coins_TD(coins, V):
    coins_required = [None] * (V + 1)
    res = min_coins_aux(coins, V, coins_required)
    print(coins_required)
    return res


def min_coins_aux(coins, V, coins_required):
    if V == 0:
        coins_required[V] = 0
        return 0
    if coins_required[V] is None:
        best_so_far = inf
        for c in coins:
            if c <= V:
                best_so_far = min(best_so_far, 1 + min_coins_aux(coins, V - c, coins_required))
        coins_required[V] = best_so_far
    return coins_required[V]
