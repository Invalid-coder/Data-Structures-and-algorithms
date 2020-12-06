#https://www.e-olymp.com/uk/submissions/7955863

import sys

INF = sys.maxsize

class Vertex:
    def __init__(self):
        self.mDistance = INF
        self.mSource = None
        self.mNeighbors = {}

    def distance(self):
        return self.mDistance

    def source(self):
        return self.mSource

    def weight(self, neighbor):
        return self.mNeighbors[neighbor]

    def neighbors(self):
        return self.mNeighbors.keys()

    def addNeighbor(self, neighbor, weight):
        self.mNeighbors[neighbor] = weight

    def setDistance(self, distance):
        self.mDistance = distance

    def setSource(self, source):
        self.mSource = source

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = Vertex()

    def addEdge(self, source, destination, weight):
        self[source].addNeighbor(destination, weight)
        self[destination].addNeighbor(source, weight)

    def __getitem__(self, item):
        return self.vertices[item]

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())

def Prim(graph):
    start = 1
    current = start
    graph[start].setDistance(0)
    remaining = set(range(1, len(graph) + 1))

    while remaining:
        vertex = graph[current]
        remaining.remove(current)

        for neighbor_key in vertex.neighbors():
            neighbor = graph[neighbor_key]
            newDist = vertex.weight(neighbor_key)

            if neighbor_key in remaining and newDist < neighbor.distance():
                neighbor.setDistance(newDist)
                neighbor.setSource(current)

        distance = INF

        for vertex_key in remaining:
            vertex = graph[vertex_key]

            if vertex.distance() < distance:
                current = vertex_key
                distance = vertex.distance()

    weight = 0

    for vertex in graph:
        source = vertex.source()

        if source is None:
            continue

        weight += vertex.weight(source)

    return weight

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination, weight = map(int, input().split())
        graph.addEdge(source, destination, weight)

    weight = Prim(graph)
    print(weight)