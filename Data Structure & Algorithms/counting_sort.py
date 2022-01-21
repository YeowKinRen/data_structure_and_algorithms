def counting_sort(l):
    """
    Time Complexity:
    O(N+U) worst case, best case, average case all are the same
    Space Complexity:
    O(N+U)
    Not Stable
    :param l:
    :return:
    """
    output = []
    count = [0] * (max(l) + 1)
    for i in l:
        count[i] += 1
    for i in range(len(count)):
        if count[i]:
            output += [i] * count[i]

    return output


if __name__ == '__main__':
    val = [3, 1, 3, 7, 5, 3, 7, 8]
    print(counting_sort(val))
