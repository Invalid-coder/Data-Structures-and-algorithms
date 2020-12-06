import sys
from Graphs.Implementation.vertex import *
from Graphs.Implementation.adjacencyList import *
from BinaryHeaps.implementation.PriorityQueue import *
from Graphs.Implementation.connectivity import *

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

def Prim(graph):
    assert not graph.isOriented
    assert check_connectivity(graph)

    start = 0 # start can be any vertex

    for vertex in graph:
        vertex.setDistance(INF)
        vertex.setSource(None)

    graph[start].setDistance(0)
    pq = PriorityQueue()

    for vertex in graph:
        pq.insert(vertex.key(), vertex.distance())

    while not pq.isEmpty():
        vertex_key = pq.extractMinimum()
        vertex = graph[vertex_key]

        for neighbor_key in vertex.neighbors():
            neighbor = graph[neighbor_key]
            newDist = vertex.weight(neighbor_key)

            if neighbor_key in pq and newDist < neighbor.distance():
                neighbor.setDistance(newDist)
                neighbor.setSource(vertex_key)
                pq.updatePriority(neighbor_key, newDist)

    spanning_tree = GraphForAlgorithm()

    for vertex in graph:
        destination = vertex.key()
        source = vertex.source()

        if source is None:
            continue

        weight = vertex.weight(source)
        spanning_tree.addEdge(source, destination, weight)

    return spanning_tree