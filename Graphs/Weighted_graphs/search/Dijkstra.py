import sys
from Graphs.Implementation.vertex import *
from Graphs.Implementation.adjacencyList import *
from BinaryHeaps.implementation.PriorityQueue import *

INF = sys.maxsize

class VertexForAlgorithm(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.mDistance = INF
        self.mSource = None

    def distance(self):
        return self.mDistance

    def setDistance(self, distance):
        self.mDistance = distance

    def source(self):
        return self.mSource

    def setSource(self, source):
        self.mSource = source

class GraphForAlgorithm(Graph):
    def __init__(self, isOriented=False):
        super().__init__(isOriented)

    def addVertex(self, vertex):
        if vertex in self:
            return False

        new_vertex = VertexForAlgorithm(vertex)
        self.mVertices[vertex] = new_vertex
        self.vertexNumber += 1

        return True

    def constructWay(self, start, end):
        if self[end].source() is None:
            return None, INF

        stack = []
        current = end

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

        return way, self[end].distance()

def Dijkstra(graph, start, end):
    for vertex in graph:
        vertex.setDistance(INF)
        vertex.setSource(None)

    graph[start].setDistance(0)
    pq = PriorityQueue()
    pq.insert(start, 0)

    fixed = [False] * len(graph)

    while not pq.isEmpty():
        vertex_key = pq.extractMinimum()
        fixed[vertex_key - 1] = True
        vertex = graph[vertex_key]

        if vertex_key == end:
            break

        for neighbor_key in vertex.neighbors():
            if fixed[neighbor_key - 1]:
                continue

            neighbor = graph[neighbor_key]
            newDist = vertex.distance() + vertex.weight(neighbor_key)

            if newDist < neighbor.distance():
                neighbor.setDistance(newDist)
                neighbor.setSource(vertex_key)

                if neighbor_key in pq:
                    pq.updatePriority(neighbor_key, newDist)
                else:
                    pq.insert(neighbor_key, newDist)

    return graph.constructWay(start, end)

if __name__ == '__main__':
    graph = GraphForAlgorithm(True)
    graph.addEdge(1, 2, 2)
    graph.addEdge(1, 3, 7)
    graph.addEdge(1, 4, 12)
    graph.addEdge(2, 3, 1)
    graph.addEdge(2, 5, 7)
    graph.addEdge(3, 5, 1)
    graph.addEdge(3, 6, 14)
    graph.addEdge(1, 2, 2)
    graph.addEdge(4, 3, 3)
    graph.addEdge(4, 6, 2)
    graph.addEdge(5, 4, 2)
    graph.addEdge(5, 6, 11)

    print(Dijkstra(graph, 1, 6))