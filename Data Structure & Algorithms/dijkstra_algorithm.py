"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Dijkstra's Algorithm
To search the shortest paths from the source to all vertices.
Introduced by computer scientist Edsger W. Dijkstra in 1956
(# will not work for graph with negative weight cycles)

Time Complexity: O(V^2)
"""
from graph import *
from queue import PriorityQueue

class Dijkstra(Graph):

    def dijkstra(self, src, dest=None):
        V = len(self.vertices)

        dist = [float('inf')] * V
        dist[src] = 0

        visited = [False] * V

        mat = self.get_adjacency_matrix()

        pq = PriorityQueue()
        pq.put((0, src))
        while not pq.empty():
            (d, u) = pq.get()
            visited[u] = True

            if u == dest:
                print(dist[u])

            for v in self.vertices[u].connected:
                v = v.key   # neighbour
                # if the adjacent vertices is not yet visited and the new_path is shorter than the old_path
                new_path = dist[u] + mat[u][v]
                old_path = dist[v]
                if visited[v] is False and old_path > new_path:
                    # update the shortest path
                    dist[v] = new_path
                    pq.put((new_path, v))
        print(dist)
        return dist


if __name__ == '__main__':
    d = Dijkstra(directed=False)
    e = [(0, 1, 4), (1, 2, 8), (2, 3, 7), (2, 8, 2), (0, 7, 8), (7, 6, 1), (6, 5, 2), (5, 4, 10)]

    for u, v, w in e:
        d.add_edge(u, v, w)
    d.dijkstra(0, 8)
    # [0, 4, 12, 19, 21, 11, 9, 8, 14]
