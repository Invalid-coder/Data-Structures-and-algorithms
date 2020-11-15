#https://www.e-olymp.com/uk/submissions/7730479

class Graph:
    def __init__(self):
        self.vertices = {}

    def addEdge(self, source, destination):
        if not source in self:
            self.vertices[source] = list()
        if not destination in self:
            self.vertices[destination] = list()

        self[source].append(destination)

    def isRecurcive(self, vertex):
        queue = [vertex]
        visited = set()
        visited.add(vertex)

        while queue:
            current = queue.pop(0)

            for neighbor in self[current]:
                if neighbor == vertex:
                    return True
                if not neighbor in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return False

    def __getitem__(self, item):
        return self.vertices[item]

    def __contains__(self, item):
        return item in self.vertices

if __name__ == '__main__':
    n = int(input())
    graph = Graph()
    sources = []

    for i in range(n):
        source = input()
        k = int(input())

        for j in range(k):
            destination = input()
            graph.addEdge(source, destination)

        if i != n - 1:
            input()

        sources.append(source)

    for source in sources:
        ans = "YES" if graph.isRecurcive(source) else "NO"
        print("{}: {}".format(source, ans))

