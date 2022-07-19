"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Z Algorithm
"""


def z_suffix(txt):
    """
    Function that implements altered Gusfield's Z Algorithm that finds the number of occurrences of the suffix
    in the text

    Time complexity:    Best case O(N) where N is the length of text
                        Worst case O(N) where N is the length of text
    :param txt: Strings which consists of lower case English letters and a delimiter, %, that separates the pattern and
                text strings
    :return: z-array which is a list of integers that stores the length of the longest suffix in text
    """
    n = len(txt)
    z = [0] * n
    r, l = n - 1, n - 1
    for k in range(n - 2, -1, -1):
        i = 0
        if k <= r:  # Case 1: If k > r
            while (k - i + 1) and txt[n - 1 - i] == txt[k - i]:
                i += 1
            z[k] = i
            if i:
                l = k  # set l to k
                r = k + 1 - i  # set r to q - 1. q = i + k
        else:  # CASE 2, if k <= r:
            if z[n - l + k - 1] < k - r + 1:  # CASE 2a, if Zk-l+1 < r - k + 1:
                z[k] = z[n - l + k - 1]  # set Zk to Zk-l+1, r & l remain unchanged.
                # print("if", z[k], k)
            elif z[n - l + k - 1] > k - r + 1:  # CASE 2b if Zk-l+1 > r - k + 1:
                z[k] = k - r - 1  # (z[i] = remaining)
            else:  # CASE 2c, if Zk-l+1 = r - k + 1:
                while (r - i - 1) and txt[r - i - 1] == txt[n - 2 - (k - r) - i]:
                    i += 1
                z[k] = k - r + i + 1
                r -= i
                l = k
    return z


def z_algorithm(txt: str):
    """
    Function that implements Gusfield's Z Algorithm that finds the number of occurrences of the prefix in the text
    eg. str = aabcaabxaay
    z       =  1003100210

    typically used in the preprocessing phase

    Time complexity:    Best case O(N) where N is the length of text
                        Worst case O(N) where N is the length of text
    :param txt: Strings which consists of lower case English letters and a delimiter, %, that separates the pattern and
                text strings
    :return: z-array which is a list of integers that stores the length of the longest prefix in text
    """
    n = len(txt)
    z = [0] * n
    r, l = 0, 0
    for k in range(1, n):
        # print(text[k])
        i = 0
        if k + 1 > r:  # Case 1: If k > r (k is outside the right-most Z-box)
            # print("case1")
            # explicit comparisons against the prefix
            while k + i < n and txt[i] == txt[k + i]:
                # print("compare")
                i += 1
            z[k] = i
            if i:
                l = k  # set l to k
                r = k + i  # set r to q - 1. q = i + k
        else:  # CASE 2, if k <= r: (k is inside the right-most Z-box)
            if z[k - l] < r - k:  # CASE 2a, if Zk-l+1 < r - k + 1: (the z value of k in the left-most Z-box does
                # not exceed the right-most Z-box)
                # print("case2a", r - k)
                z[k] = z[k - l]  # set Zk to Zk-l+1, r & l remain unchanged.
            elif z[k - l] > r - k:  # CASE 2b if Zk-l+1 > r - k + 1:
                # print("case 2b")
                z[k] = r - k  # (z[i] = remaining)
            else:  # CASE 2c, if Zk-l+1 = r - k + 1:
                # print("case2c?")
                while r + i <= n and txt[r + i - 1] == txt[r - k + i - 1]:
                    # print("compare")
                    i += 1
                z[k] = r - k + i - 1
                r += i - 1
                l = k

    return z

if __name__ == '__main__':
    print(z_algorithm("aab$baabaa"))

    # [0, 1, 0, 0, 0, 3, 1, 0, 2, 1]
    print(z_algorithm("aabcaabxaay"))
    # [0, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]