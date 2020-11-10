#https://www.e-olymp.com/uk/submissions/7685809

class Graph:
    def __init__(self, n):
        self.verticesDegree = [0] * n

    def addEdge(self, source, destination):
        self.verticesDegree[source] += 1
        self.verticesDegree[destination] += 1

    def __iter__(self):
        return iter(self.verticesDegree)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for i in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source - 1, destination - 1)

    for degree in graph:
        print(degree)