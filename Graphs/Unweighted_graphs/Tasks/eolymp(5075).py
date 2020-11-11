#https://www.e-olymp.com/uk/submissions/7685705

class Vertex:
    def __init__(self):
        self.inputs = 0
        self.outputs = 0

    def __str__(self):
        return str(self.inputs) + " " + str(self.outputs)

class Graph:
    def __init__(self, n):
        self.mVertices = {}

        for i in range(1, n + 1):
            self.mVertices[i] = Vertex()

    def addEdge(self, source, destination):
        self.mVertices[source].outputs += 1
        self.mVertices[destination].inputs += 1

    def __iter__(self):
        return iter(self.mVertices.values())

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    for vertex in graph:
        print(vertex)


