#https://www.e-olymp.com/uk/submissions/7687509

class Graph:
    def __init__(self, n):
        self.adjacentMatrix = []

        for i in range(n):
            self.adjacentMatrix.append([0] * n)

    def addEdge(self, source, destination):
        self.adjacentMatrix[source][destination] = 1

    def __iter__(self):
        return iter(self.adjacentMatrix)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for i in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source - 1, destination - 1)

    for row in graph:
        print(*row)