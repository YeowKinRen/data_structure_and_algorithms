def naive_pattern_matching(txt: str, pat: str):
    n = len(txt)
    m = len(pat)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if txt[i + j - 1] != pat[j]:
                break  # mismatch
            j += 1
        if j == m:
            print(i)


if __name__ == '__main__':
    naive_pattern_matching("aaaaaaaaaa", "aaa")
