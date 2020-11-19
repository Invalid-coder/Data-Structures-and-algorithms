#https://www.e-olymp.com/uk/submissions/7768036

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def isConnected(self, deleted_edges):
        remaining = set(self.vertices.keys())
        stack = [remaining.pop()]

        while stack:
            current = stack.pop()

            for neighbor in self[current]:
                if neighbor in remaining:
                    if not (current, neighbor) in deleted_edges and \
                        not (neighbor, current) in deleted_edges:
                        stack.append(neighbor)
                        remaining.remove(neighbor)

        return not remaining

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)
    edges = []

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)
        edges.append((source, destination))

    k = int(input())

    for _ in range(k):
        data = tuple(map(int, input().split()))[1:]
        deleted_edges = [edges[i - 1] for i in data]

        print("Connected" if graph.isConnected(deleted_edges) else "Disconnected")
