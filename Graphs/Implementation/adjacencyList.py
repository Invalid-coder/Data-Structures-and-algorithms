from Graphs.Implementation.vertex import *

class Graph:
    def __init__(self, isOriented=False):
        self.isOriented = isOriented
        self.vertexNumber = 0
        self.mVertices = {}

    def addVertex(self, vertex):
        if vertex in self:
            return

        new_vertex = Vertex(vertex)
        self.mVertices[vertex] = new_vertex
        self.vertexNumber += 1

    def getVertex(self, vertex):
        assert vertex in self

        key = vertex.key() if isinstance(vertex, Vertex) else vertex
        return self.mVertices[key]

    def vertices(self):
        return self.mVertices

    def addEdge(self, source, destination, weight=1):
        if not source in self:
            self.addVertex(source)
        if not destination in self:
            self.addVertex(destination)

        self[source].addNeightbor(destination, weight)

        if not self.isOriented:
            self[destination].addNeightbor(source, weight)

    def setData(self, vertex, data):
        assert vertex in self

        self[vertex].setData(data)

    def getData(self, vertex):
        assert vertex in self
        return self[vertex].data()

    def transpose(self):
        g_inv = Graph(self.isOriented)

        for vertex in self:
            for neighbor_key in vertex.neighbors():
                g_inv.addEdge(neighbor_key, vertex.key())

        return g_inv

    def __contains__(self, vertex):
        if isinstance(vertex, Vertex):
            return vertex.key() in self.mVertices
        else:
            return vertex in self.mVertices

    def __iter__(self):
        return iter(self.mVertices.values())

    def __len__(self):
        return self.vertexNumber

    def __getitem__(self, vertex):
        return self.getVertex(vertex)

if __name__ == '__main__':
    graph = Graph()
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(2, 5)
    graph.addEdge(3, 5)
    graph.addEdge(3, 6)
    graph.addEdge(4, 3)
    graph.addEdge(4, 6)
    graph.addEdge(5, 4)
    graph.addEdge(5, 6)