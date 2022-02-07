"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Edit distance (Levenshtein distance)
"""


def dist(s1, m, s2, n):
    # base case: empty strings (case 1)
    if m == 0:
        return n

    if n == 0:
        return m

    # if the last characters of the strings match (case 2)
    if s1[m - 1] == s2[n - 1]:
        cost = 0
    else:
        cost = 1

    return min(dist(s1, m - 1, s2, n) + 1,  # deletion (case 3a))
               dist(s1, m, s2, n - 1) + 1,  # insertion (case 3b))
               dist(s1, m - 1, s2, n - 1) + cost)  # substitution (case 2 + 3c)


def dist_dp(s1, s2):
    """O(m*n)"""
    (m, n) = (len(s1), len(s2))
    memo = [[0]*(n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        memo[i][0] = i  # (case 1)
    for j in range(1, n + 1):
        memo[0][j] = j  # (case 1)

    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):

        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  # (case 2)
                cost = 0  # (case 2)
            else:
                cost = 1  # (case 3c)

            memo[i][j] = min(memo[i - 1][j] + 1,  # deletion (case 3b)
                          memo[i][j - 1] + 1,  # insertion (case 3a)
                          memo[i - 1][j - 1] + cost)  # replace (case 2 + 3c)

    return memo[m][n]


if __name__ == '__main__':
    str1 = 'kitten'
    str2 = 'sitting'

    print('The Levenshtein distance is', dist(str1, len(str1), str2, len(str2)))
    print('The Levenshtein distance is', dist_dp(str1, str2))
