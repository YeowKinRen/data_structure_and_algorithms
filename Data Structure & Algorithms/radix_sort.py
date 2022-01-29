"""
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.

Radix Sort
"""


def counting_sort(array, place):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    # Calculate count of elements
    for i in range(n):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = n - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        array[i] = output[i]


def radix_sort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10


if __name__ == '__main__':
    data = [121, 432, 564, 23, 1, 45, 788]
    radix_sort(data)
    print(data)
