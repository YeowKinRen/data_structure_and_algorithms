"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################
Depth First Search

Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.

"""
from graph import *


class DFS(Graph):

    def dfs(self, source, visited=None):
        path = [source]
        if visited is None:
            visited = {source}
        vertex = self.vertices[source]
        for v in vertex.connected:
            v = v.key
            if v not in visited:
                print(v, visited)
                visited.add(v)
                x, visited = self.dfs(v, visited)
                path += x
            else:
                return path, visited
        print(path)


if __name__ == '__main__':
    dfs = DFS()
    dfs.add_edge(0, 1)
    dfs.add_edge(0, 2)
    dfs.add_edge(1, 2)
    dfs.add_edge(2, 0)
    dfs.add_edge(2, 3)
    dfs.add_edge(3, 3)
    dfs.print_graph()
    dfs.dfs(2)
