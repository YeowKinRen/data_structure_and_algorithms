# https://www.spoj.com/problems/FIBOSUM/

# from typing import List
# import numpy as np
# Matrix = np.matrix
#
# MOD = 10 ** 9 + 7
#
#
# def power(mat: Matrix, n: int) -> Matrix:
#     res = np.identity(len(mat), dtype=np.int64)
#
#     while n:
#         if n & 1:
#             np.matmul(res, mat, out=res)
#             res %= MOD
#
#         np.matmul(mat, mat, out=mat)
#         mat %= MOD # Required for numpy if you want correct results
#         n >>= 1
#
#     return res
#
#
# def fib(n: int) -> int:
#     if n == 0:
#         return 0
#
#     magic = np.matrix([[1, 1], [1, 0]], dtype=np.int64)
#     mat = power(magic, n - 1)
#     return mat[0,0]
#
#
# if __name__ == '__main__':
#     print(fib(10 ** 18))



class Mat:
    def __init__(self, n):
        self.n = n
        self.m = [[0] * self.n for _ in range(self.n)]

    def identity(self):
        for i in range(self.n):
            self.m[i][i] = 1

    def __mul__(self, a):
        res = Mat(self.n)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    res.m[i][j] += self.m[i][k] * a.m[k][j]
                    res.m[i][j] %= int(1e9 + 7)
        return res


def fib(n):
    res = Mat(2)
    res.identity()
    T = Mat(2)
    T.m[0][0], T.m[0][1], T.m[1][0] = 1, 1, 1
    if n <= 2:
        return 1
    n -= 2
    # log(n)
    while n:
        if n & 1:
            res = res * T
        T = T * T
        n //= 2
    return (res.m[0][0] + res.m[0][1]) % int(mod)


def fibosum(n, m):
    return (fib(m + 2) - fib(n + 1) + int(mod)) % int(mod)


def fib2(n):
    # base case
    if n == -1:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1

    res = Mat(3)
    res.identity()
    T = Mat(3)
    T.m[0][0], T.m[0][1], T.m[0][2] = 1, 1, 1
    T.m[1][1], T.m[1][2] = 1, 1
    T.m[2][1] = 1

    # n >= 2
    n -= 1

    # log(n)
    while n:
        if n & 1:
            res = res * T
        T = T * T
        n //= 2

    return (res.m[0][0] + res.m[0][1]) % int(mod)


def fibosum2(n, m):
    return (fib2(m) - fib2(n - 1) + int(mod)) % int(mod)