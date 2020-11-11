class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self.vertices[source].append(destination)

    def waysSearch(self, start, end):
        sources = {start:None}
        queue = [start]

        while queue:
            current = queue.pop(0)

            for neighbor in self.vertices[current]:
                pass

if __name__ == '__main__':
    n, k, a, b, d = map(int, input().split())

    for i in range(k):
        source, destination = map(int, input().split())
