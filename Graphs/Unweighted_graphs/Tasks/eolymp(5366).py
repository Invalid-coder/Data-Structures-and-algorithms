class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def amountOfChildren(self, vertex):
        return len(self[vertex])

    def isRoot(self, vertex, maxAmount):
        if len(self[vertex]) == maxAmount:
            return True
        else:
            return False

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n = int(input())
    graph = Graph(n)

    for _ in range(n - 1):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    roots = []
    maxAmount = 0

    for i in range(1, n + 1):
        maxAmount = max(maxAmount, graph.amountOfChildren(i))

    for i in range(1, n + 1):
        if graph.isRoot(i, maxAmount):
            roots.append(i)

    print(*roots)
