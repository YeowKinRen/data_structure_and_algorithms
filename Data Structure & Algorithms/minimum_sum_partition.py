"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Minimum Sum Partition

"""


def min_sum_partition(l):
    """Dynamic Programming implementation O(N^2)"""
    total = sum(l) // 2 + 1
    memo = [False] * total
    memo[0] = True
    for index, i in enumerate(l):
        for j in range(total - 1, i - 1, -1):
            # print(index, i,"enter     ",j)
            if memo[j - 1]:
                # print(j)
                memo[j] = True
    for j in range(total - 1, -1, -1):
        if memo[j]:
            # print(sum(arr))
            return sum(arr) - 1 * j  # sum(arr) - j


if __name__ == '__main__':
    arr = [1, 2, 2, 2, 3]
    print(min_sum_partition(arr))

