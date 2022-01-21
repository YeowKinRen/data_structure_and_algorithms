"""
Minimum Sum Partition

"""


def min_sum_partition(l):
    """Dynamic Programming implementation O(N^2)"""
    total = sum(l) // 2 + 1
    memo = [False] * total
    memo[0] = True
    for index, i in enumerate(l):
        for j in range(total - 1, i - 1, -1):
            # print(index, i,"enter     ",j)
            if memo[j - 1]:
                # print(j)
                memo[j] = True
    for j in range(total - 1, -1, -1):
        if memo[j]:
            # print(sum(arr))
            return sum(arr) - 1 * j  # sum(arr) - j


if __name__ == '__main__':
    arr = [1, 2, 2, 2, 3]
    print(min_sum_partition(arr))

"""
This problem is very similar to the 0/1 Knapsack problem although it can be further optimized but I will explain a non-optimized one because it is simpler to understand.
Given a list, [1, 2, 2, 2, 3], as in Knapsack, the memoization is a 2D array of size, (n + 1) x (sum + 1), where n is the size of the input list and sum is the sum of all the elements in the input list.
In the memoization array, we are going to store Boolean values (True/False).
A True in the memoization array at index (i, j) means that using the first i elements in the input list, we are able to generate a subset with sum of j.
A False in the memoization array at index (i, j) means that using the first i elements in the input list, we are not able to generate a subset with sum of j.
The table above shows the base cases.
The first column means that we are able to generate a subset of sum of 0 using the elements.
In the first row, after the first True, the rest are False. This is because the first row has no elements to use to build a subset. Therefore, it is impossible to generate a subset with a sum greater than 0.
The decision function is just an inclusion/exclusion.
The recurrence relation is
memo[i][j] = memo[i - 1][j] OR memo[i - 1][j - lst[i - 1]] 
I want to partition a set into 2 subsets such that the difference between the subset sums is minimum.
In other words, I want the subset sums to be as close as sum // 2.
"""
