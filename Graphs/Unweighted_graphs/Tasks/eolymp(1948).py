#https://www.e-olymp.com/uk/submissions/7768837

WHITE = 0
GRAY = 1
BLACK = 2

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)

    def dfs(self, start, colors, stack):
        if colors[start] == BLACK:
            return

        if colors[start] == GRAY:
            raise Exception("Cycle was found!")

        colors[start] = GRAY

        for neighbor in self[start]:
            self.dfs(neighbor, colors, stack)

        colors[start] = BLACK
        stack.append(start)

    def topologicalSorting(self):
        vertirces = self.vertices.keys()
        colors = {key:WHITE for key in vertirces}
        stack = []

        for key in vertirces:
            self.dfs(key, colors, stack)

        sequence = []

        while stack:
            sequence.append(stack.pop())

        return sequence

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    try:
        print(*graph.topologicalSorting())
    except Exception:
        print(-1)