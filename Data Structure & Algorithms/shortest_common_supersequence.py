"""

"""


def shortest_supersequence_n(s1, s2):
    """Naive implementation"""
    # Length of the shortest supersequence =
    # (Sum of lengths of given two strings) - (Length of LCS of two given strings)
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
    return m + n - max_len


def shortest_supersequence_r(s1, s2, m, n):
    """Recursive implementation O(2^(m+n))"""
    if m == 0 or n == 0:
        return n + m

    if s1[m - 1] == s2[n - 1]:
        return shortest_supersequence_r(s1, s2, m - 1, n - 1) + 1

    return min(shortest_supersequence_r(s1, s2, m, n - 1) + 1, shortest_supersequence_r(s1, s2, m - 1, n) + 1)


def shortest_supersequence_dp(s1, s2):
    m = len(s2)
    n = len(s1)
    memo = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        memo[i][0] = i
    for j in range(m + 1):
        memo[0][j] = j

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                memo[i + 1][j + 1] = memo[i][j] + 1
            else:
                memo[i + 1][j + 1] = min(memo[i][j + 1]+1, memo[i + 1][j]+1)
    return memo[n][m]


if __name__ == '__main__':
    str1 = "ABCBDAB"
    str2 = "BDCABA"

    print(shortest_supersequence_n(str1, str2))
    print(shortest_supersequence_r(str1, str2, len(str1), len(str2)))
    print(shortest_supersequence_dp(str1, str2))
