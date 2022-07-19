# https://www.codechef.com/problems/ABX01
def power9(a, n):
    if n == 0:
        return 1
    p = power9(a, n // 2)
    p = (p * p) % 9
    if n % 2:
        p = (p * a) % 9
    return p


def solve(A, N):
    ans = power9(A, N)
    if not ans:
        ans = 9
    return ans
