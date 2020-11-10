from Graphs.Implementation.vertexBase import *

class Vertex(VertexBase):
    def __init__(self, key):
        super().__init__(key)
        self.mNeighbors = {}

    def addNeightbor(self, vertex, weight=1):
        if isinstance(vertex, VertexBase):
            self.mNeighbors[vertex.key()] = weight
        else:
            self.mNeighbors[vertex] = weight

    def neighbors(self):
        return self.mNeighbors.keys()

    def weight(self, neighbor):
        if isinstance(neighbor, VertexBase):
            return self.mNeighbors[neighbor.key()]
        else:
            return self.mNeighbors[neighbor]