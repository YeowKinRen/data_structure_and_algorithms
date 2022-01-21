"""
2-Sum Problem
"""


# Naive method to find a pair in a list with given sum
def two_sum_n(array, sum):
    output = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == sum:
                output.append((i, j))
    return output


# Sort method
def two_sum_s(array, sum):
    A = sorted(array)
    low, high = 0, len(A) - 1
    output = []
    while low < high:
        if A[low] + A[high] == sum:
            output.append((low, high))
            low, high = low + 1, high - 1
        if A[low] + A[high] < sum:
            low = low + 1
        elif A[low] + A[high] > sum:
            high = high - 1
    return output, A


# hash method to find a pair in a list with given sum
def two_sum_d(array, sum):
    dict_a = {}
    output = []
    for i, e in enumerate(array):
        if sum - e in dict_a:
            output.append((dict_a[sum - e], i))
        dict_a[e] = i
    return output


# Find pair with given sum in the list
if __name__ == '__main__':
    input = [8, 7, 2, 5, 3, 1]
    sum = 10
    print(two_sum_n(input, sum))
    print(two_sum_s(input, sum))
    print(two_sum_d(input, sum))
