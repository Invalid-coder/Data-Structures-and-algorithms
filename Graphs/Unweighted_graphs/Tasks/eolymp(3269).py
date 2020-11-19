class Vertex:
    def __init__(self):
        self.neighbors = {}

    def addNeighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def getNeighbors(self):
        return self.neighbors.items()

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = Vertex()

    def addEdge(self, source, destination, w):
        self[source].addNeighbor(destination, w)
        self[destination].addNeighbor(source, w)

    def dfs(self, visited, start, weights):
        visited.add(start)

        for neighbor, weight in self[start].getNeighbors():
            if not neighbor in visited:
                if not neighbor in weights:
                    weights[neighbor] = weights[start] + weight
                else:
                    weights[neighbor] = max(weights[neighbor], weights[start] + weight)

                self.dfs(visited, neighbor, weights)

        visited.remove(start)

    def getWeight(self, source, destination):
        visited = set()
        weights = {source: 0}
        self.dfs(visited, source, weights)

        return weights[destination]

    """
        def get_weight(self, v, u):
        weights = {v: 0}
        queue = [v]

        while queue:
            current = queue.pop(0)

            for neighbor, weight in self[current].getNeighbors():
                if not neighbor in weights:
                    weights[neighbor] = weights[current] + weight
                    queue.append(neighbor)

        return weights[u]
    """

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m, q = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination, weight = map(int, input().split())
        graph.addEdge(source, destination, weight)

    A = [tuple(map(int, input().split())) for _ in range(n)]
    B = [tuple(map(int, input().split())) for _ in range(n)]

    for _ in range(q):
        source, destination = map(int, input().split())
        weight = graph.getWeight(source, destination)
        minW, maxW = B[source - 1][destination - 1], A[source - 1][destination - 1]

        if minW <= weight and weight <= maxW:
            print("Yes %.7f" % weight)
        else:
            print("No")
