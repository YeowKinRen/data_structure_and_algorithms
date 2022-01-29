"""
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.

Longest Increasing Subsequence Problem
"""


def lis_b(arr):
    """https://en.wikipedia.org/wiki/Longest_increasing_subsequence
    Arrays and Binary searching implementation
     O(NlogN)"""

    n = len(arr)
    size = 0
    M = [0] * n  # Stores the index k of the smallest value arr[k]
    P = [0] * n  # Stores the index of the predecessor of arr[k]
    for i in range(n):
        lo, hi = 1, size + 1
        while lo < hi:
            m = lo + (hi - lo) // 2
            if arr[M[m]] < arr[i]:
                lo = m + 1
            else:
                hi = m
        P[i] = M[lo - 1]
        M[lo] = i

        size = max(lo, size)

    # Reconstruct the longest increasing subsequence
    S = [0] * size
    k = M[size]
    for i in range(size - 1, -1, -1):
        S[i] = arr[k]
        k = P[k]

    return size


def lis_dp(arr):
    """dynamic programming implementation"""
    n = len(arr)
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print("Length of lis is", lis_b(arr))
    print("Length of lis is", lis_dp(arr))
