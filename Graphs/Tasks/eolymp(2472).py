#https://www.e-olymp.com/uk/submissions/7685084

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self.getNeighbors(source).append(destination)
        self.getNeighbors(destination).append(source)

    def getNeighbors(self, vertex):
        return self.vertices[vertex]

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    graph = Graph(n)

    for _ in range(k):
        data = tuple(map(int, input().split()))

        if data[0] == 1:
            graph.addEdge(data[1], data[2])
        else:
            print(*graph.getNeighbors(data[1]))