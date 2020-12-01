import sys
from Graphs.Implementation.vertex import *
from Graphs.Implementation.adjacencyList import *
from BinaryHeaps.implementation.PriorityQueue import *

INF = sys.maxsize

class VertexWithHeuristic(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.mDistance = INF
        self.mSource = None
        self.mHeuristicValue = 0

    def distance(self):
        return self.mDistance

    def setDistance(self, distance):
        self.mDistance = distance

    def source(self):
        return self.mSource

    def setSource(self, source):
        self.mSource = source

    def heuristic(self):
        return self.mHeuristicValue

    def calcuateHeuristic(self, other):
        position = self.mData

        if isinstance(other, Vertex):
            dest_position = other.data()
        else:
            dest_position = other

        assert position is not None and dest_position is not None

        self.mHeuristicValue = ((dest_position[0] - position[0]) ** 2 +
                                (dest_position[1] - position[1])) ** 0.5


class PlainGraph(Graph):
    def __init__(self, isOriented=False):
        super().__init__(isOriented)

    def addEdge(self, source, destination):
        weight = self.distance(source, destination)
        super().addEdge(source, destination, weight)

    def addVertex(self, vertex):
        if vertex in self:
            return False

        new_vertex = VertexWithHeuristic(vertex)
        self.mVertices[vertex] = new_vertex
        self.vertexNumber += 1

        return True

    def distance(self, source, destination):
        source_position = self.getData(source)
        destination_position = self.getData(destination)

        assert source_position is not None and destination_position is not None
        return (((destination_position[0] - source_position[0]) ** 2) + (
                    (destination_position[1] - source_position[1]) ** 2)) ** 0.5

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

def AStar(graph, start, end):
    for vertex in graph:
        vertex.setDistance(INF)
        vertex.setSource(None)
        vertex.calculateHeuristic(graph[end])

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
                h = neighbor.heuristic()
                f = newDist + h

                if neighbor_key in pq:
                    pq.updatePriority(neighbor_key, f)
                else:
                    pq.insert(neighbor_key, f)

    return graph.constructWay(start, end)