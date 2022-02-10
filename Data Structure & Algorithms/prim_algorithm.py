"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Prim's Algorithm
To find the minimum spanning tree from a weighted graph.

Introduced by computer scientist Edsger W. Dijkstra in 1956
(# will not work for graph with negative weight cycles)
(# implemented using a priority queue data structure)
Time Complexity: O(V^2)
"""
from graph import *
from queue import PriorityQueue


class Prim(Graph):

    def printMST(self, parent, mat):
        print("Edge \tWeight")
        for i in range(1, len(self.vertices)):
            print(parent[i], "-", i, "\t", mat[i][parent[i]])

    def prim(self):
        V = len(self.vertices)
        parent = [None] * V
        mat = self.get_adjacency_matrix()

        key = [float('inf')] * V
        key[0] = 0  # Select a random starting vertex
        pq = PriorityQueue()
        pq.put((0, 0))
        mstSet = [False] * V

        parent[0] = -1
        while not pq.empty():
            print(pq.queue)
            (d, u) = pq.get()
            mstSet[u] = True

            for v in self.vertices[u].connected:
                v = v.key  # neighbour

                if mat[u][v] < key[v] and mstSet[v] is False:
                    pq.put((mat[u][v], v))
                    key[v] = mat[u][v]
                    parent[v] = u

        print(parent)
        self.printMST(parent, mat)
        return parent


if __name__ == '__main__':
    d = Prim(directed=False)
    e = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (2, 3, 4), (3, 4, 9)]

    for u, v, w in e:
        d.add_edge(u, v, w)
    d.prim()
