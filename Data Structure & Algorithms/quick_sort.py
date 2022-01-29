"""
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.

Quick sort
Worst-case performance	O(n^2)
Best-case performance	O(nlogn)
A divide-and-conquer algorithm based on a partitioning routine recursive calls.

Lomuto’s Partition Scheme: maintains index i as it scans the array using another index j such that the elements at lo
through i-1 (inclusive) are < the pivot, and the elements at i through j (inclusive) are >= the pivot
Hoare’s Partition Scheme: 2 pointers move toward each other, until inversion
"""


def quicksort_l(arr, lo, hi):
    if lo < hi:
        p = partition_l(arr, lo, hi)
        quicksort_l(arr, lo, p - 1)
        quicksort_l(arr, p + 1, hi)


def partition_l(arr, lo, hi):
    """Lomuto partition scheme
    Chooses the last element as the pivot
    """
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    i = i + 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def quicksort_h(arr, lo, hi):
    if 0 <= lo < hi and hi >= 0:
        p = partition_h(arr, lo, hi)
        quicksort_h(arr, lo, p)
        quicksort_h(arr, p + 1, hi)


def partition_h(arr, lo, hi):
    """Hoare partition scheme"""
    pivot = arr[(hi + lo) // 2]
    i = lo - 1
    j = hi + 1

    while True:
        while True:
            i += 1
            if not arr[i] < pivot:
                break
        while True:
            j -= 1
            if not arr[j] > pivot:
                break
        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    l = [12, 11, 13, 5, 6, 7]
    quicksort_l(l, 0, 5)
    print(l)

    l = [12, 11, 13, 14, 17, 5, 6, 7]
    quicksort_h(l, 0, 7)
    print(l)
