"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Bucket sort

Worst-case performance:	O(NlogN)
Average performance: O(N+(N^2/K)+K) where k is the number of buckets.
Worst-case space complexity	O(N+K)
Distribution sort

"""


def bucket_sort(arr):
    # buckets ← new array of k empty lists
    n = len(arr)

    k = 9
    bucket = [[] for _ in range(k)]

    # M ← the maximum key value in the array
    m = max(arr)

    # for i = 0 to length(array) do
    #     insert array[i] into buckets[floor(k × array[i] / M)]
    for i in range(n):
        index_b = k * arr[i] // (m+1)
        bucket[index_b].append(arr[i])

    # for i = 0 to k do
    #     nextSort(buckets[i])
    for i in range(k):
        bucket[i] = sorted(bucket[i])

    # return the concatenation of buckets[0], ...., buckets[k]
    index = 0
    for i in range(k):
        for j in range(len(bucket[i])):
            arr[index] = bucket[i][j]
            index += 1
    return arr


if __name__ == '__main__':
    array = [40, 12, 31, 27, 25, 8, 1, 32, 17]
    print(array)
    print(bucket_sort(array))
    print(array)
