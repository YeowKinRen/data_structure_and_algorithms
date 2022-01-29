"""
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.

Rabin-Karp Algorithm
"""

def rabin_karp(pat, txt, q=101):
    """
    Implementation of Rabin Karp Algorithm (Pattern Searching by rolling hash)
    Time complexity:    Best case: O(N+M) where N is the length of the text
                        and M is the length of the pattern.
                        Worst case: O(NM) where N is the length of the text
                        and M is the length of the pattern.

    :param pat: pattern String
    :param txt: text String
    :param q: prime modulus
    :return: The list of indexes of all pattern occurrence in text
    """
    m = len(pat)
    n = len(txt)
    b = 256  # base, the size of the character set
    p = 0  # the hash value for pattern
    t = 0  # the hash value for text
    h = 1
    pattern = []

    for _ in range(m - 1):  # The value of h would be "pow(d, m-1)%q"
        h = (h * b) % q

    for i in range(m):  # Calculate the hash value of pattern and first window of text
        p = (b * p + ord(pat[i])) % q
        t = (b * t + ord(txt[i])) % q

    for i in range(n - m + 1):  # Slide the pattern over text one by one
        if p == t:

            check = True
            for j in range(m):      # Check for characters one by one
                if txt[i + j] != pat[j]:
                    check = False
                    break

            if check:   # if p == t and pat[0...m-1] = txt[i, i+1, ...i+m-1]
                pattern.append(i)

        if i < n - m:               # Calculate hash value for next window of text
            t = (b * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q   # Remove leading char, add trailing char
            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t + q
    return pattern


if __name__ == '__main__':
    txt = "abcdababxmnacb"
    pat = "ab"

    print("Pattern found at index ", *rabin_karp(pat, txt))
