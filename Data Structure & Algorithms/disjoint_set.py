""""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Disjoint-set data structure
Time complexity:
Union by size: O(log(N))
Union by rank: O(log(N))
"""


class DisjointSet:
    def __init__(self, V, edgeFile, union_by="rank"):
        if union_by == "rank":
            self.rank = True
        elif union_by == "size":
            self.rank = False
        else:   # default rank
            self.rank = True
        self.edgeList = edgeFile
        self.V = V
        self.parent = [-1] * V

    def find(self, a):
        """
        Path Compression
        Determine the root of the subset a particular vertex, a, is in.

        Precondition: None
        Time complexity:    Best case: O(h) when h is height of the path
                            Worst case: O(h) when h is height of the path
        Space complexity: O(1)
        Aux space complexity: O(1)
        :param a: An integer, which is index of a vertex in the parent list
        :return: An integer, which is the root of the subset
        """

        if self.parent[a] < 0:  # root is reached
            return a
        else:
            root = self.find(self.parent[a])
            self.parent[a] = root
            return root

    def union(self, a, b):
        """
        The joining of 2 subsets to a single subset

        Precondition: None
        Time complexity:    Best case: O(h) where h is the maximum height of the paths
                            Worst case: O(h) where h is the maximum height of the paths
        Space complexity: O(1)
        Aux space complexity: O(1)
        :param a: An integer, which is index of a vertex, a, in the parent list
        :param b: An integer, which is index of a vertex, b, in the parent list
        :return: True or false depending on the operation
        """
        root_a = self.find(a)  # find root of tree containing `a'
        root_b = self.find(b)  # find root of tree containing `b'
        if root_a == root_b:
            return False                    # `a' and `b' in the same tree
        height_a = -self.parent[root_a]  # height of tree containing `a'
        height_b = -self.parent[root_b]  # height of tree containing `b'
        if height_a > height_b:
            if not self.rank:
                self.parent[root_a] = -(height_b + height_a)  # update to size
            self.parent[root_b] = root_a  # link shorter tree's root to taller
        elif height_b > height_a:
            if not self.rank:
                self.parent[root_b] = -(height_b + height_a)  # update to size
            self.parent[root_a] = root_b
        else:  # if (height_a == height_b)
            self.parent[root_a] = root_b
            if self.rank:

                self.parent[root_b] = -(height_b + 1)  # update to height
            else:
                self.parent[root_b] = -(height_b + height_a)  # update to size
        return True


if __name__ == '__main__':
    obj = DisjointSet(5, [(0, 2), (4, 2), (3, 1)])
    obj.union(0, 2)
    obj.union(4, 2)
    obj.union(3, 1)
    if obj.find(4) == obj.find(0):
        print('Yes')
    else:
        print('No')
    if obj.find(1) == obj.find(0):
        print('Yes')
    else:
        print('No')

