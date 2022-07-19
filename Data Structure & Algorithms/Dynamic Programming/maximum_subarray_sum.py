"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################
Maximum Subarray Sum Problem
"""


def max_subarray_sum_n(l):
    """Naive implementation O(N^2)"""
    max_sum = 0
    start = 0
    end = 0
    n = len(l)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):

            curr_sum += l[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start = i
                end = j + 1
    return l[start:end], max_sum


def max_subarray_sum_ka(l):
    """Kadane’s Algorithm Implementation (Dynamic Programming) O(N)"""
    n = len(l)
    start = 0
    end = 0
    max_sum = 0
    curr_sum = 0

    for i in range(n):
        curr_sum += l[i]
        if curr_sum > max_sum:
            end = i + 1
            max_sum = curr_sum
        if curr_sum < 0:  # if the sum is negative then the
            start = i + 1  # the next element is the starting position
            curr_sum = 0
    return l[start:end], max_sum


if __name__ == '__main__':
    l = [-3, -4, 5, -1, 2, -4, 6, -1]
    print("Subarray {} sum {}".format(*max_subarray_sum_n(l)))
    print("Subarray {} sum {}".format(*max_subarray_sum_ka(l)))
