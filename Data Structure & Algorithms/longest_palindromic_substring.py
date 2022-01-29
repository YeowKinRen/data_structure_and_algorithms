"""
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.

Longest Palindromic Substring Problem
"""

def is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def longest_palindrome_n(s):
    """Naive implementation O(N^3)"""
    best_len = 0
    best_s = ""
    n = len(s)
    for l in range(n):
        for r in range(l, n):
            curr_len = r - l + 1
            subs = s[l:curr_len]
            if curr_len > best_len and is_palindrome(subs):
                best_len = curr_len
                best_s = subs
    return best_s


def longest_palindrome_dp(s):
    """Dynamic Programming implementation O(N^2)"""
    n = len(s)
    best_len = 1
    start = 0
    memo = [[0] * n for _ in range(n)]
    for i in range(n):
        memo[i][i] = 1

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            best_len = 2
            memo[i][i + 1] = 1
            start = i

    for k in range(3, n + 1):  # k denotes the length of the substring
        for i in range(n - k + 1):
            j = i + k - 1  # i, j denotes the start and end of the substring
            if memo[i + 1][j - 1] and s[i] == s[j]:
                memo[i][j] = 1
                if k > best_len:
                    start = i
                    best_len = k
    return s[start:start + best_len]


def longest_palindrome(s):
    """Expand Around Center implementation O(N^2)"""
    best_len = 1
    start = 0
    n = len(s)
    for i in range(1, n):
        # Find the longest even length palindrome with center points as i-1 and i.
        l, r = i - 1, i
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        curr_len = r - l + 1
        if s[l] == s[r] and curr_len > best_len:
            start = l
            best_len = curr_len
        # Find the longest odd length palindrome with center points as i-1 and i+1.
        l, r = i - 1, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        curr_len = r - l + 1
        if s[l] == s[r] and curr_len > best_len:
            start = l
            best_len = curr_len
    return s[start:start + best_len]


def modify(s):
    n = len(s)
    s_mod = []
    for i in range(n):
        s_mod.append("#")
        s_mod.append(s[i])
    s_mod.append("#")
    return "".join(s_mod)


def longest_palindrome_ma(s):
    """Manacher’s Algorithm implementation O(N)"""
    s_mod = modify(s)  # modify the string to insert unique character
    print(len(s_mod))
    n = 2 * len(s) + 1
    p = [0] * n
    p[1] = 1
    c = 1  # current center position
    r = 2  # current rightmost position
    best_len = 0
    max_center = 0
    for i in range(2, n):
        mirror = (2 * c) - i
        if i < r:
            p[i] = min(r - i, p[mirror])
        a = i + (1 + p[i])
        b = i - (1 + p[i])
        while a < n and b >= 0 and s_mod[a] == s_mod[b]:
            p[i] += 1
            a += 1
            b -= 1
        if i + p[i] > r:
            c = i
            r = i + p[i]

            if p[i] > best_len:
                best_len = p[i]
                max_center = i

    start = (max_center - best_len) // 2
    return s[start:start + best_len]


if __name__ == '__main__':
    string = "AASALASAAP"
    print(longest_palindrome_n(string))
    print(longest_palindrome_dp(string))
    print(longest_palindrome_ma(string))
    print(longest_palindrome(string))
