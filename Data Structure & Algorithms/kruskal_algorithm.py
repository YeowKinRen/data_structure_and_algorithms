"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Kruskal's Algorithm
To find the minimum spanning tree from a weighted graph.


"""
from disjoint_set import *



class Kruskal(DisjointSet):

    def kruskals(self):
        """
        A greedy algorithm to obtain the minimum spanning tree of that graph connecting all the vertices together

        Precondition: None
        Time complexity:    Best case: O(n) where n is the number of vertex in the parent list
                            Worst case: O(n) where n is the number of vertex in the parent list
        Space complexity: O(n) where n is the number of vertex in the parent list
        Aux space complexity: O(n) where n is the number of vertex in the parent list
        :return: An integer of the total weight of a minimum spanning tree in G and a list of the edges of the
        minimum weight spanning found
        """
        weight = 0
        mst = []
        self.edgeList = sorted(self.edgeList, key=lambda x: x[2])
        for i in range(len(self.edgeList)):
            x = self.union(self.edgeList[i][0], self.edgeList[i][1])
            if x:
                mst.append(self.edgeList[i])
                weight += self.edgeList[i][2]
        return weight, mst
