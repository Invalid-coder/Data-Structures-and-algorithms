#https://www.e-olymp.com/uk/submissions/7901116

import sys

INF = sys.maxsize

class Vertex:
    def __init__(self):
        self.mDistance = INF
        self.mSource = None
        self.mNeighbors = {}

    def addNeighbor(self, neighbor, weight):
        self.mNeighbors[neighbor] = weight

    def weight(self, neighbor):
        return self.mNeighbors[neighbor]

    def neighbors(self):
        return self.mNeighbors.keys()

    def distance(self):
        return self.mDistance

    def setDistance(self, distance):
        self.mDistance = distance

    def source(self):
        return self.mSource

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

    def Dijkstra(self, start, finish):
        visited = [False] * len(self)
        self[start].setDistance(0)
        current = start

        while True:
            visited[current - 1] = True
            vertex = self[current]

            for neighbor_key in vertex.neighbors():
                if not visited[neighbor_key - 1]:
                    neighbor = self[neighbor_key]
                    newDist = vertex.distance() + vertex.weight(neighbor_key)

                    if newDist < neighbor.distance():
                        neighbor.setDistance(newDist)
                        neighbor.setSource(current)

            distance = INF

            for neighbor_key in vertex.neighbors():
                if not visited[neighbor_key - 1] and self[neighbor_key].distance() < distance:
                    current = neighbor_key
                    distance = self[neighbor_key].distance()

            if distance == INF:
                break

        return self.constructWay(start, finish)

    def constructWay(self, start, finish):
        if self[finish].source() is None:
            return None

        stack = []
        current = finish

        while True:
            stack.append(current)

            if current == start:
                break

            current = self[current].source()

            if current is None:
                return None

        way = []

        while stack:
            way.append(stack.pop())

        return self[finish].distance(), way

    def __len__(self):
        return len(self.vertices)

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    s, f = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination, weight = map(int, input().split())
        graph.addEdge(source, destination, weight)

    ans = graph.Dijkstra(s, f)

    if ans:
        print(ans[0])
        print(*ans[1])
    else:
        print(-1)