"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################



right-to-left scanning
bad character shift rule
good suffix shift rule


Use (extended) bad-character rule to find how many places to the
right pat should be shifted under txt. Call this amount nbadcharacter.

Use good suffix rule to find how many places to the right pat should
be shifted under txt. Call this amount ngoodsuffix.

Shift pat to the right under txt by max(nbadcharacter; ngoodsuffix)
places.
"""


def z_suffix(text):
    """
    Function that implements altered Gusfield's Z Algorithm that finds the number of occurrences of the suffix
    in the text

    Time complexity:    Best case O(N) where N is the length of text
                        Worst case O(N) where N is the length of text
    :param text: Strings which consists of binary
    :return: z-array which is a list of integers that stores the length of the longest suffix in text
    """
    n = len(text)
    z = [0] * (n + 1)
    r, l = n - 1, n - 1
    for k in range(n - 2, -1, -1):
        i = 0
        if k <= r:  # Case 1: If k > r
            while (k - i + 1) and text[n - 1 - i] == text[k - i]:
                i += 1
            z[k] = i
            if i:
                l = k  # set l to k
                r = k + 1 - i  # set r to q - 1. q = i + k
        else:  # CASE 2, if k <= r:
            if z[n - l + k - 1] < k - r + 1:  # CASE 2a, if Zk-l+1 < r - k + 1:
                z[k] = z[n - l + k - 1]  # set Zk to Zk-l+1, r & l remain unchanged.
            elif z[n - l + k - 1] > k - r + 1:  # CASE 2b if Zk-l+1 > r - k + 1:
                z[k] = k - r - 1  # (z[i] = remaining)
            else:  # CASE 2c, if Zk-l+1 = r - k + 1:
                while (r - i) and text[r - i - 1] == text[n - 2 - (k - r) - i]:
                    i += 1
                z[k] = k - r + i + 1
                r -= i
                l = k
    z[n] = n
    return z


def bad_character(text):
    """
    Function that computes the bad character table

    Time complexity:    Best case O(N) where N is the length of text
                        Worst case O(N) where N is the length of text
    :param text: Strings
    :return: bad character table, list of integers
    """
    n = len(text)
    bc = [[0 for _ in range(n)] for _ in range(57)]
    for i in range(n - 1, -1, -1):
        j = 1
        bc[ord(text[i]) - 65][i] = i + 1
        while i + j < n and bc[ord(text[i]) - 65][i + j] == 0:
            bc[ord(text[i]) - 65][i + j] = i + 1
            j += 1
    return bc


def good_suffix(m, zs):
    """
    Function that computes the good suffix values

    Time complexity:    Best case O(N) where N is the length of zs
                        Worst case O(N) where N is the length of zs
    :param m: length of zs - 1
    :param zs: z suffix, list of integers
    :return: good suffix, list of integers
    """
    gs = [0] * (m + 1)
    for p in range(m - 1):
        j = m - zs[p]
        gs[j] = p + 1
    return gs


def match_prefix(m, zs):
    """
    Function that computes the match prefix values

    Time complexity:    Best case O(N) where N is the length of zs
                        Worst case O(N) where N is the length of zs
    :param m: length of zs - 1
    :param zs: z suffix, list of integers
    :return: matched prefix, list of integers
    """
    mp = [0] * (m + 1)
    for i in range(m - 1):
        if zs[i] == i + 1:
            mp[m - i - 1] = i + 1
        else:
            mp[m - i - 1] = mp[m - i]
    mp[0] = m
    return mp


def boyer_moore(txt: str, pat: str):
    """
    Function that implement Boyer-Moore's Algorithm for pattern matching

    :param txt: Strings
    :param pat: Strings
    :return:
    """
    n = len(txt)
    m = len(pat)
    zs = z_suffix(pat)
    gs = good_suffix(m, zs)
    mp = match_prefix(m, zs)
    bc = bad_character(pat)
    k = m - 1
    start, stop = -1, -1
    shift = 1
    output = []
    comparison = 0
    while k < n:
        i = 0
        while i < m and txt[k - i] == pat[m - 1 - i]:
            print(txt[k - i], pat[m - 1 - i])
            i += 1
            comparison += 1
            if k - i == stop:   # Galil's optimisation
                print("Galil's optimisation",i, start, stop)
                i += min(m-i, stop-start)
        if i == m:  # Exact match
            output.append(k - m + 1)
            start, stop = k - (m - mp[1])-1, k
            # print("***", k - (m - mp[1]), k)
            shift = (m - mp[1])

        # elif i > m:
        #     print("something wrong")
        else:  # Mismatch
            bc_shift = max(1, m-1 - i - bc[ord(txt[k - i]) - 97][m - i - 1])
            # print(txt[k - i], k, i, m-1 - i - bc[ord(txt[k - i]) - 97][m - i - 1])
            bc_start = k - i - 1
            bc_stop = k - i
            if gs[m - i] > 0:  # Case 1a: if a mismatch occurs at some pat[k] and googsuffix(k+1)>0
                gs_shift = m - gs[m - i]  # shift pat by m - goodsuffix(k+1) places
                gs_start = k - i - 1  # start = gs[m - i] - m + k + 1
                gs_stop = k  # stop = gs[m - i]
                # print("here?", gs_shift)
            else:  # Case 1b: if a mismatch occurs at some pat[k], and goodsuffix(k + 1)=0 (match prefix)
                gs_shift = m - mp[m - i]  # matchprefix(k+1): length of largest suffix of pat identical to prefix
                gs_start = k - (m - mp[m - i]) + 1  # start = 1
                gs_stop = k  # stop = mp[m - i]
                # print("###", gs_shift)
            print(gs_shift, bc_shift)
            if bc_shift > gs_shift:
                shift = bc_shift
                start, stop = bc_start, bc_stop
            else:    # bcShift <= gsShift:
                shift = gs_shift
                start, stop = gs_start, gs_stop
        k += shift
            # print("k", k - shift, "shift", shift, stop, "--->",start)
    # print(comparison)
    return output


if __name__ == '__main__':
    # text = "xpbctbxabacbxtbpqa"
    txt = "01234567890123456789012345"
    txt = "CGTGCCTACTTACTTACTTACGCGAA"
    txt = "ANPANMAN"
    # txt = "abaaabcd"
    pat = "CTTACTTAC"
    pat = "PAN"
    # pat = "abc"
    print(boyer_moore(txt, pat))
