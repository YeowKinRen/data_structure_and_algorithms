# LOCKER - Magic of the locker
# https://www.spoj.com/problems/LOCKER/
# why 3? https://palak001.medium.com/spoj-locker-magic-of-the-locker-a758bccf432f

def power(a, n):
    mod = 1000000007
    if n == 0:
        return 1
    p = power(a, n // 2)
    p = (p * p) % mod
    if n % 2:
        p = (p * a) % mod
    return p


def locker(n):
    mod = 1000000007
    ans = 1
    if n < 2:

        ans = n
    else:
        cnt = n // 3
        rem = n % 3
        if rem == 1:
            ans = (power(3, cnt - 1) * 4) % mod

        else:
            if rem == 2:
                ans = (power(3, cnt) * 2) % mod

            else:  # rem = 0
                ans = power(3, cnt)

    return ans


if __name__ == '__main__':
    print(locker(4))
    print(locker(5))
