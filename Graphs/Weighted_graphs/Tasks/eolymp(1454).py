import sys

INF = sys.maxsize

class Vertex:
    def __init__(self):
        self.mDistance = INF
        self.mNeighbors = {}

    def neighbors(self):
        return self.mNeighbors.keys()

    def addNeighbor(self, neighbor, weight):
        if not neighbor in self.mNeighbors:
            self.mNeighbors[neighbor] = [weight]
        else:
            self.mNeighbors[neighbor].append(weight)

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

def BelmanFord(graph, start, end):
    graph[start].setDistance(0)

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor_key in vertex.neighbors():
                neighbor = graph[neighbor_key]

                for weight in vertex.weight(neighbor_key):
                    newDist = vertex.distance() + weight

                    if neighbor.distance() == INF or newDist > neighbor.distance():
                        neighbor.setDistance(newDist)

    for vertex in graph:
        for neighbor_key in vertex.neighbors():
            neighbor = graph[neighbor_key]

            for weight in vertex.weight(neighbor_key):
                newDist = vertex.distance() + weight

                if newDist > neighbor.distance():
                    return ":)"

    if graph[end].distance() == INF:
        return ':('
    else:
        return graph[end].distance()

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination, weight = map(int, input().split())
        graph.addEdge(source, destination, weight)

    ans = BelmanFord(graph, 1, n)

    print(ans)