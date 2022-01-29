"""
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.

0-1 Knapsack Problem
"""


def knapsack(weight, value, N):
    memo = [[0]*(N + 1) for _ in range(len(weight) + 1)]
    # for every row (item)
    for i in range(1, len(weight) + 1):
        # for every column (weight)
        for j in range(1, N + 1):
            # get the exclude at the current weight (row above)
            exclude = memo[i - 1][j]
            # calculate the include
            include = 0
            if weight[i - 1] <= j:
                include = value[i - 1] + memo[i - 1][j - weight[i - 1]]
            memo[i][j] = max(exclude, include)
    print(memo)
    return memo[len(weight) - 1][N]


if __name__ == '__main__':
    weight = [6, 1, 5, 9]
    value = [230, 40, 350, 550]
    N = 12
    print(knapsack(weight, value, N))
