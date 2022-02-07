"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Longest Common Subsequence Problem
"""


def longest_subsequence_n(s1, s2):
    """Naive implementation O(N*(M + N))"""
    m = len(s2)
    n = len(s1)
    max_len = 0
    i = 0

    while i < n:
        curr_len = 0
        k = i
        j = 0
        while j < m and k < n:
            if s1[k] == s2[j]:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
                k += 1
                j += 1
            elif j < m - 1:
                j += 1
            elif k < n - 1:
                k += 1
            else:
                break
        i += 1
    return max_len


def longest_subsequence_r(s1, s2, m, n):
    """Recursive implementation """
    if m == 0 or n == 0:
        return 0

    if s1[m - 1] == s2[n - 1]:
        return longest_subsequence_r(s1, s2, m - 1, n - 1) + 1

    return max(longest_subsequence_r(s1, s2, m, n - 1), longest_subsequence_r(s1, s2, m - 1, n))


def longest_subsequence_dp(s1, s2):
    """Dynamic Programming implementation O(N*M)"""
    m = len(s2)
    n = len(s1)
    memo = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                memo[i + 1][j + 1] = memo[i][j] + 1
            else:
                memo[i + 1][j + 1] = max(memo[i][j + 1], memo[i + 1][j])

    return memo[n][m]


if __name__ == '__main__':
    str1 = "ABCBDAB"
    str2 = "BDCABA"
    print("The length of the LCS is", longest_subsequence_n(str1, str2))
    print("The length of the LCS is", longest_subsequence_dp(str1, str2))
