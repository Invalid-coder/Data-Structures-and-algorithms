import sys

INF = sys.maxsize

class Vertex:
    def __init__(self):
        self.mDistance = INF
        self.mNeighbors = {}

    def neighbors(self):
        return self.mNeighbors.keys()

    def addNeighbor(self, neighbor, weight):
        self.mNeighbors[neighbor] = weight

    def distance(self):
        return self.mDistance

    def setDistance(self, distance):
        self.mDistance = distance

    def weight(self, neighbor):
        return self.mNeighbors[neighbor]

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = Vertex()

    def addEdge(self, source, destination, weight):
        self[source].addNeighbor(destination, weight)

    def __getitem__(self, item):
        return self.vertices[item]

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())

def Dijkstra(graph, start, finish):
    graph[start].setDistance(0)
    fixed = [False] * len(graph)
    current = start

    while True:
        fixed[current - 1] = True

        if current == finish:
            break

        vertex = graph[current]

        for neighbor_key in vertex.neighbors():
            if fixed[neighbor_key - 1]:
                continue

            neighbor = graph[neighbor_key]
            newDist = vertex.distance() + vertex.weight(neighbor_key)

            if newDist < neighbor.distance():
                neighbor.setDistance(newDist)

        distance = INF

        for neighbor_key in vertex.neighbors():
            neighbor = graph[neighbor_key]

            if not fixed[neighbor_key - 1] and neighbor.distance() < distance:
                current = neighbor_key
                distance = neighbor.distance()

        if distance == INF:
            break

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination, weight = map(int, input().split())
        graph.addEdge(source, destination, weight)

    Dijkstra(graph, 1, n)

    if graph[n].distance() == INF:
        print(-1)
    else:
        print(graph[n].distance())