class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)

    def removeEdge(self, source, destination):
        self[source].remove(destination)

    def isConnected(self):
        remaining = set(self.vertices.keys())
        stack = [remaining.pop()]

        while stack:
            current = stack.pop()

            for neighbor in self[current]:
                if neighbor in remaining:
                    stack.append(neighbor)
                    remaining.remove(neighbor)

        return not remaining

    def transpose(self):
        graph_inv = Graph(len(self.vertices))

        for vertex in self.vertices.keys():
            for neighbor in self[vertex]:
                graph_inv.addEdge(neighbor, vertex)

        return graph_inv

    def isStrongConnected(self):
        if not self.isConnected():
            return False

        graph_inv = self.transpose()

        return graph_inv.isConnected()

    def addEdges(self, edges):
        added_edges = []
        weight = 0

        for i, edge in enumerate(edges):
            self.addEdge(edge[0], edge[1])

            if self.isStrongConnected():
                added_edges.append(i + 1)
                weight += edge[2]
            else:
                self.removeEdge(edge[0], edge[1])

        return weight, added_edges

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = Graph(n)

    for i in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    k = int(input())
    edges = []

    for i in range(k):
        edge = tuple(map(int, input().split()))
        edges.append(edge)

    weight, edges = graph.addEdges(edges)

    if weight:
        print("YES")
        print(weight)
        print(len(edges))

        for edge in edges:
            print(edge)
    else:
        print("NO")
