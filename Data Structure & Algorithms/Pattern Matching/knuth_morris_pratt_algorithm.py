"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Knuth Morris Pratt Algorithm

Time Complexity: O(n + m)

Using Gusfield's z-algorithm to obtain the longest proper suffix that matches a
prefix

Compare pat[1 : : :m] against any region of txt[j ... j + m - 1] in the
natural left-to-right direction (unlike Boyer-Moore).
if the first mismatch, while scanning left-to-right, occurs at pos i + 1:

    Shift pat to the right (relative to txt) by KMP shift rule
    Shift pat by exactly i - SPi places to the right.
else, in the case an occurrence of pat is found in txt,
    then shift pat by m - SPm places.
"""
from gusfields_z_algorithm import z_algorithm


def knuth_morris_pratt(pat: str, txt: str):
    """
    Function that implement Knuth Morris Pratt Algorithm for pattern matching

    :param txt: Strings
    :param pat: Strings
    :return:
    """
    m = len(pat)
    n = len(txt)

    sp = [0] * m  # the length of the longest proper suffix that matches prefix
    z = z_algorithm(pat)
    # print(z)
    for j in range(m - 1, 0, -1):
        sp[j + z[j] - 1] = z[j]
    # print(sp)
    i = 0   # the length of pattern matched of pat[j:i+i] and txt[j:i+i]
    j = 0   # txt
    while i + j < n:
        print(j)
        while i < m and pat[i] == txt[i + j]:
            i += 1
            # x += 1
        if i == 0:
            print("if")
            j += (i + 1)
            i = 0
        elif i == m:
            print("Found pattern at index", j)
            j += m - sp[m - 1]
            i = sp[m - 1]
        else: # elif i < m:
            # print(j, i - sp[i-1], sp[i-1])
            print("elif")
            j += i - sp[i - 1]
            i = sp[i - 1]


if __name__ == '__main__':
    # txt = "ABABDABACDABABCABAB"
    txt = "xabxyabxyabxz"
    # pat = "ABABCABAB"
    pat = "abxyabxz"

    txt = "GTTATAGCTGATCGCGGCGTAGCGGCGA"
    pat =           "GTAGCGGCG"

    txt = "AABAACAADAABAABA"
    pat = "AABA"
    knuth_morris_pratt(pat, txt)
