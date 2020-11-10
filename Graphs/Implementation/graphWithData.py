from Graphs.Implementation.adjacentMatrix import *

class GraphWithData(Graph):
    DEFAULT_VERTEX_DATA = 0

    def __init__(self, isOriented=False, vertices=20):
        super().__init__(isOriented, vertices)

        self.data = [self.DEFAULT_VERTEX_DATA] * self.vertex_number

    def setData(self, vertex, data):
        assert 0 <= vertex < self.vertex_number

        self.data[vertex] = data

    def getData(self, vertex):
        assert 0 <= vertex < self.vertex_number

        return self.data[vertex]

if __name__ == '__main__':
    graph = GraphWithData(True, 7)
    graph.setData(1, 7)
    graph.setData(2, 3)
    graph.setData(3, 4)
    graph.setData(4, 7)
    graph.setData(5, 1)
    graph.setData(6, 9)
    graph.addEdge(1, 2, 2)
    graph.addEdge(1, 3, 7)
    graph.addEdge(1, 4, 12)
    graph.addEdge(2, 3, 5)
    graph.addEdge(2, 5, 7)
    graph.addEdge(3, 5, 1)
    graph.addEdge(3, 6, 1)
    graph.addEdge(4, 3, 3)
    graph.addEdge(4, 6, 4)
    graph.addEdge(5, 4, 7)
    graph.addEdge(5, 6, 1)