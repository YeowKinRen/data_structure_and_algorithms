"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################
Breadth First Search

Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.

"""
from graph import *


class BFS(Graph):

    def bfs(self, source,):
        queue = [source]
        visited = {source}
        path = [source]
        while queue:
            vertex = self.vertices[queue.pop(0)]
            for v in vertex.connected:
                v = v.key
                if v not in visited:
                    print(v, visited)
                    path += [v]
                    queue.append(v)
                    visited.add(v)
        print(path)




if __name__ == '__main__':
    bfs = BFS()
    bfs.add_edge(0, 1)
    bfs.add_edge(0, 2)
    bfs.add_edge(1, 2)
    bfs.add_edge(2, 0)
    bfs.add_edge(2, 3)
    bfs.add_edge(3, 3)
    bfs.print_graph()
    bfs.bfs(2)
