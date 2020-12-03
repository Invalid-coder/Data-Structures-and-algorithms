#https://www.e-olymp.com/uk/submissions/7917288

import sys

INF = sys.maxsize

class Vertex:
    def __init__(self):
        self.mNeighbors = {}
        self.mDistance = INF

    def distance(self):
        return self.mDistance

    def setDistance(self, distance):
        self.mDistance = distance

    def addNeighbor(self, neighbor, weight):
        self.mNeighbors[neighbor] = weight

    def weight(self, neighbor):
        return self.mNeighbors[neighbor]

    def neighbors(self):
        return self.mNeighbors.keys()

class Graph:
    def __init__(self, n):
        self.mVertices = {}

        for i in range(n):
            self.mVertices[i] = Vertex()

    def addEdge(self, source, destination, weight):
        self[source].addNeighbor(destination, weight)

    def BelmanFord(self, start):
        self[start].setDistance(0)

        for i in range(len(self) - 1):
            for vertex in self:
                for neighbor_key in vertex.neighbors():
                    neighbor = self[neighbor_key]
                    newDist = vertex.distance() + vertex.weight(neighbor_key)

                    if newDist < neighbor.distance():
                        neighbor.setDistance(newDist)

        for vertex in self:
            for neighbor_key in vertex.neighbors():
                neighbor = self[neighbor_key]
                newDist = vertex.distance() + vertex.weight(neighbor_key)

                if newDist < neighbor.distance():
                    return True

        return False

    def __getitem__(self, item):
        return self.mVertices[item]

    def __iter__(self):
        return iter(self.mVertices.values())

    def __len__(self):
        return len(self.mVertices)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination, weight = map(int, input().split())
        graph.addEdge(source, destination, weight)

    ans = graph.BelmanFord(0)

    print("possible" if ans else "not possible")
