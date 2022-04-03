import math
from typing import List


def unique_2n_plus_1(arr):
    # Given 2n + 1 numbers, where every number is coming twice except one number
    # Find the unique number
    xor = 0
    for i in arr:
        xor ^= i
    return xor


def unique_2n_plus_2(arr):
    # Given 2n + 2 numbers, where every number is coming twice except 2 numbers
    # Find the unique numbers
    xor = 0
    for i in arr:
        xor ^= i

    pos = 0  # find the pos of the first set bit
    temp = xor
    while (temp & 1) == 0:
        pos += 1
        temp = temp >> 1

    set_a = 0  # filter out the numbers form the array which have set bit at pos
    set_b = 0
    mask = 1 << pos
    for i in range(len(arr)):
        if arr[i] & mask > 0:
            set_a = set_a ^ arr[i]
        else:
            set_b = set_b ^ arr[i]
    return set_a, set_b


def unique_3n_plus_1(arr):
    # Given 3n + 1 numbers, where every number is coming thrice except one number
    # Find the unique number
    sum_arr = [0] * 32  # fill constructor
    for x in arr:

        for i in range(32):  # extract all bits of x
            ith_bit = x & (1 << i)
            if ith_bit:
                sum_arr[i] += 1
    for i in range(32):  # array of bits
        sum_arr[i] = sum_arr[i] % 3
    num = 0
    for i in range(32):
        num += sum_arr[i] * (1 << i)  # (?)* 2^(i)
    return num


def generate_all_subseq(string):
    # print all subsequences of a string using bit-masking
    n = len(string)
    for i in range((1 << n)):
        j = 0
        while i > 0:
            last_bit = i & 1
            if last_bit:
                print(string[j], end="")
            j += 1
            i = i >> 1
        print()
    return string


def matrix_score(mat):
    """
    You are given an m x n binary matrix grid.
    A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
    Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
    Return the highest possible score after making any number of moves (including zero moves).
    https://www.youtube.com/watch?v=8tcPTkVgJq8
    """
    n = len(mat)
    m = len(mat[0])
    ans = (1 << (m - 1)) * n
    print(ans)
    for j in range(1, m):
        val = 1 << (m - 1 - j)
        sets = 0
        for i in range(n):
            if mat[i][j] == mat[i][0]:
                sets += 1
        ans += max(sets, n - sets) * val
    return ans


def count_triplets(arr):
    """
    Given an integer array nums, return the number of AND triples.
    An AND triple is a triple of indices (i, j, k) such that:
    0 <= i < nums.length
    0 <= j < nums.length
    0 <= k < nums.length
    nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.
    https://www.youtube.com/watch?v=tEmYcyxZxe8
    https://www.youtube.com/watch?v=7ibf14FeknE
    """
    dic = {}
    n = len(arr)
    for i in range(n):
        for j in range(n):
            val = arr[i] & arr[j]
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1
    ans = 0
    for i in range(n):
        for key in dic:
            if (key & arr[i]) == 0:
                ans += dic[key]
    return ans


def range_bitwise_and(m, n):
    """
    Given two integers left and right that represent the range [left, right],
    return the bitwise AND of all numbers in this range, inclusive.
    https://leetcode.com/problems/bitwise-and-of-numbers-range/
    https://www.youtube.com/watch?v=6aHmj9ihjMY
    """
    diff = n - m
    ans = 0
    for i in range(31):
        val = 1 << i  # 2^i
        if diff // val == 0:  # if
            if (n & val) & (m & val):
                ans += val
    return ans


def total_hamming_distance(arr):
    """
    https://leetcode.com/problems/total-hamming-distance/
    :param arr:
    :return:
    """
    ans = 0
    n = len(arr)
    for i in range(31):
        ones = 0
        zeros = 0
        val = 1 << i
        for j in range(n):
            if arr[j] & val:
                ones += 1
            else:
                zeros += 1
        ans += ones * zeros
    return ans


def tsp(dist, set_of_cities, city, n):
    # base case
    if set_of_cities == ((1 << n) - 1):  # return the cost from the city to the original
        return dist[city][0]
    ans = math.inf
    for choice in range(n):
        if set_of_cities & (1 << choice) == 0:  # check if city is visited
            # set of cities 0001|0010 = 0011
            sub_prob = dist[city][choice] + tsp(dist, set_of_cities | (1 << choice), choice, n)
            ans = min(ans, sub_prob)
    return ans


def tsp_dp(dist, set_of_cities, city, n, dp):
    # base case
    if set_of_cities == ((1 << n) - 1):  # return the cost from the city to the original
        return dist[city][0]
    if len(dp[set_of_cities][city]) != 0:
        return dp[set_of_cities][city]
    ans = math.inf
    for choice in range(n):
        if set_of_cities & (1 << choice) == 0:  # check if city is visited

            sub_prob = dist[city][choice] + tsp(dist, set_of_cities | (1 << choice), choice, n, dp)
            ans = min(ans, sub_prob)
    dp[set_of_cities][city] = ans
    return ans


def decode(encoded: List[int]) -> List[int]:
    """
    https://dev.to/seanpgallivan/solution-decode-xored-permutation-41c2#:~:text=Leetcode%20Problem%20%231734%20(Medium)%3A%20Decode%20XORed%20Permutation&text=There%20is%20an%20integer%20array,perm%5Bi%20%2B%201%5D%20.
    https://leetcode.com/problems/decode-xored-permutation/
    """
    n = len(encoded)
    val1 = 0
    val = 0
    ans = [0] * (n + 1)
    for i in range(1, n + 2):
        val1 ^= i
    for i in range(0, n):
        if i % 2:
            val ^= encoded[i]
    ans[0] = val ^ val1
    for i in range(1, n + 1):
        ans[i] = ans[i - 1] ^ encoded[i - 1]

    return ans


n = 0
ans = ""

def solve(pos, val, dp, v):
    global ans
    global n
    if val == 0:
        return ""
    if len(dp[pos][val]) != 0:
        return dp[pos][val]
    ans = ""
    for i in range(n):
        val1 = 1 << i
        if val & val1:
            str = v[pos][i] + solve(i, val ^ val1, dp, v)
            if len(ans):
                ans = str if (len(ans) > len(str)) else ans
            else:
                ans = str
    dp[pos][val] = ans
    return ans


def shortestSuperstring(words):
    global n
    global ans
    n = len(words)
    v = [n * [""] for _ in range(n)]
    go_to_break = False
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            str = words[j]
            for k in range(len(words[i])):
                str1 = words[i][k:]
                for k1 in range(1, len(words[j])):
                    str2 = words[j][0:0+k1]
                    if str1 == str2:
                        str = words[j][k1:]
                        go_to_break = True
                        break
                if go_to_break:
                    break
            v[i][j] = str
            go_to_break = False
    val = 1 << n
    val -= 1
    dp = [n * [""] for i in range(n)]
    for i in range(n):
        str = words[i]
        str += solve(i, val ^ (1 << i), dp, v)
        if len(ans):
            ans = str if len(ans) > len(str) else ans
        else:
            ans = str
    return ans


if __name__ == '__main__':
    print(unique_2n_plus_1([]))
    print(unique_2n_plus_2([2, 3, 4, 5, 4, 3, 7, 2]))
    print(unique_3n_plus_1([1, 3, 5, 4, 3, 1, 5, 5, 3, 1]))
    print(generate_all_subseq("abcd"))
    print(matrix_score([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
    print(count_triplets([2, 1, 3]))
    print(range_bitwise_and(5, 7))
    dist = [[0, 20, 42, 25], [20, 0, 30, 34], [42, 30, 0, 10], [25, 34, 10, 0]]
    print(tsp(dist, 1, 0, 4))
    dp = [-1] * 4
    # print(tsp_dp(dist, 1, 0, 4, dp))
    print(decode([2, 1]))
    w = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
    # Output: "gctaagttcatgcatc"
    print(shortestSuperstring(w))
