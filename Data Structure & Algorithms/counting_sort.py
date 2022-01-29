"""
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.

Counting Sort
"""


def counting_sort(array, in_place=False):
    """
    Time Complexity: O(N+U) where N is the size of input array and U is the domain size.
    Space Complexity: O(N+U)
    Stable sort
    :param in_place:
    :param array:
    :return:
    """
    n = len(array)
    output = [0] * n
    count = [0] * (max(array) + 1)

    # histogram computation
    for i in range(n):
        count[array[i]] += 1
    # prefix sum computation
    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(n - 1, -1, -1):
        count[array[i]] -= 1
        output[count[array[i]]] = array[i]

    if in_place:
        for i in range(n):
            array[i] = output[i]
    return output


if __name__ == '__main__':
    val = [3, 1, 3, 7, 5, 3, 7, 8]

    print(counting_sort(val, in_place=True))
    print(val)
