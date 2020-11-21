import math

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = set()

    def addEdge(self, source, destination):
        self[source].add(destination)
        self[destination].add(source)

    def __getitem__(self, item):
        return self.vertices[item]

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == '__main__':
    n, r = map(int, input().split())
    graph = Graph(n)
    coords = []

    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))

    curr = 0

    while curr < n - 1:
        for vertex in range(curr + 1, n):
            if distance(*coords[curr], *coords[vertex]) <= r:
                graph.addEdge(curr + 1, vertex + 1)

        curr += 1

    remaining = set(graph.vertices.keys())
    ans = []

    while remaining:
        vertex = max(remaining, key=lambda x: len(graph[x]))# vertex with biggest amount of neighbors
        remaining.remove(vertex)
        remaining -= graph[vertex] # neighbors of vertex are included in the tower's radious
                                   # so we dont need to place towers in them
        ans.append(vertex) # put the tower in vertex

    print(len(ans))
    print(*sorted(ans))
