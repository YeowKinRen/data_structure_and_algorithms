"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Merge Sort
"""


def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1


def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, s)


if __name__ == '__main__':
    l = [12, 11, 13, 5, 6, 7]
    merge_sort(l)
    print(l)
