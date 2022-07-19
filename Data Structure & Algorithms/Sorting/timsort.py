"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Timsort
A hybrid stable sorting algorithm, derived from merge sort and insertion sort.

Best Case:  	O(N)
Average Case:	O(Nlog(N))
Worst Case: 	O(Nlog(N))
Stable: Yes
In-place: Yes

Algorithm

Step 1 - Divide the array into the number of blocks (run).
Step 2 - Consider the size of run, either 32 or 64.
Step 3 - Sort the individual elements of every run one by one using insertion sort.
Step 4 - Merge the sorted runs one by one using the merge function of merge sort.
Step 5 - Double the size of merged sub-arrays after every iteration.

 [40, 10, 20, 42, 27, 25, 1, 19]
        /                \
[40, 10, 20, 42]  [27, 25, 1, 19]
       |                 |
[10, 20, 40, 42]  [1, 19, 25, 27]
        \               /
[1, 10, 19, 20, 25, 27, 40, 42]

"""

MINRUN = 4  # n/MINRUN in the power of 2 (usually 32 to 64)


def binary_search(arr, item, start, end):
    if start == end:
        if arr[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] < item:
        return binary_search(arr, item, mid + 1, end)
    elif arr[mid] > item:
        return binary_search(arr, item, start, mid - 1)
    else:
        return mid


def insertion_sort(arr, left, right):
    """Binary Insertion Sort"""
    print(arr[left:right+1])
    for i in range(left + 1, right + 1):
        j = i - 1
        selected = arr[i]
        loc = binary_search(arr, selected, 0, j)
        while j >= loc:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = selected
        print(arr[left:right + 1])


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(len1):
        left.append(arr[l + i])
    for i in range(len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timsort(arr):
    """
    """
    n = len(arr)
    for i in range(0, n, MINRUN):
        end = min(i + MINRUN - 1, n - 1)
        insertion_sort(arr, i, end)
    print(arr)
    size = MINRUN
    while size < n:
        for l in range(0, n, 2 * size):
            m = min((l + size - 1), (n - 1))  # mid, to ensure
            r = min((l + 2 * size - 1), (n - 1))  # right to ensure the
            if m < r:
                merge(arr, l, m, r)
        size *= 2


if __name__ == '__main__':
    array = [40, 12, 31, 27, 25, 8, 1, 32, 17]
    print(array)
    timsort(array)
    print(array)
