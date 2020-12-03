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
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = Vertex()

    def addEdge(self, source, destination, weight):
        self[source].addNeighbor(destination, weight)

    def Dijkstra(self, start, end):
        fixed = [False] * len(self)
        self[start].setDistance(0)
        current = start

        while True:
            fixed[current - 1] = True

            if current == end:
                break

            vertex = self[current]

            for neighbor_key in vertex.neighbors():
                neighbor = self[neighbor_key]
                newDist = vertex.distance() + vertex.weight(neighbor_key)

                if newDist < neighbor.distance():
                    neighbor.setDistance(newDist)

            distance = INF

            for neighbor_key in vertex.neighbors():
                neighbor = self[neighbor_key]

                if not fixed[neighbor_key - 1] and neighbor.distance() <= distance:
                    current = neighbor_key
                    distance = neighbor.distance()

            if distance == INF:
                break

        return self[end].distance()

    def __getitem__(self, item):
        return self.vertices[item]

    def __len__(self):
        return len(self.vertices)

if __name__ == '__main__':
    n = int(input())
    weights = list(map(int, input().split()))
    m = int(input())

    if m != 0:
        edges = list(map(int, input().split()))
        graph = Graph(n)
        i = 0

        while i < 2 * m:
            source, destination = edges[i], edges[i + 1]
            graph.addEdge(source, destination, weights[source - 1])
            graph.addEdge(destination, source, weights[destination - 1])
            i += 2

        ans = graph.Dijkstra(1, n)

        if ans == INF:
            print(-1)
        else:
            print(ans)
    else:
        print(-1)