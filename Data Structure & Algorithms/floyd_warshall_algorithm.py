"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Floyd–Warshall algorithm
To search the shortest paths in a directed weighted graph with positive or negative edge weights
To compute the transitive closure of the graph

Time Complexity: O(V^3)
"""
from graph import *


class FloydWarshall(Graph):

    def floyd_warshall(self):
        # create adjacency matrix
        V = len(self.vertices)
        dist = [[float('inf')]*V for _ in range(V)]
        for e in self.edges:
            u, v, w = e
            dist[u][v] = w
        for i in range(V):
            dist[i][i] = 0
        # print(dist)
        for k in range(V):  # intermediate vertex
            for i in range(V):  # source vertex
                for j in range(V):  # destination vertex
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist





if __name__ == '__main__':
    fw = FloydWarshall()
    fw.add_edge(0, 1, 5)
    fw.add_edge(0, 3, 10)
    fw.add_edge(1, 2, 3)
    fw.add_edge(2, 3, 1)
    fw.print_graph()
    fw.floyd_warshall()
