class Graph:
    def __init__(self, isOriented=False, vertex_number=20):
        self.isOriented = isOriented
        self.vertex_number = vertex_number
        self.adjacentMatrix = []

        for i in range(self.vertex_number):
            self.adjacentMatrix.append([0] * self.vertex_number)

    def addEdge(self, source, destination, weight=1):
        assert 0 <= source < self.vertex_number and 0 <= destination < self.vertex_number

        self.adjacentMatrix[source][destination] = weight

        if not self.isOriented:
            self.adjacentMatrix[destination][source] = weight

if __name__ == '__main__':
    graph = Graph(True, 7)
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