"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Implementation of Graph Abstract Data Type (ADT)


"""


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected[nbr] = weight


# class Edge:
#     def __init__(self, u, v):
#         self.origin = u
#         self.destination = v


class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        # self.outgoing = {}
        # self.incoming = {} if directed else self.outgoing
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def add_edge(self, u, v, weight=0):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.vertices[u].add_neighbor(self.vertices[v], weight)
        if not self.directed:
            self.vertices[v].add_neighbor(self.vertices[u], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def print_graph(self):
        for v in self.vertices:
            src = self.vertices[v]
            for dest in src.connected:
                print(f'({src.key} —> {dest.key}, weight: {src.connected[dest]}) ')
            # print()


if __name__ == '__main__':
    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10), (4, 5, 1), (5, 4, 3)]
    g = Graph()
    for u, v, w in edges:
        g.add_edge(u, v, w)
    g.print_graph()
