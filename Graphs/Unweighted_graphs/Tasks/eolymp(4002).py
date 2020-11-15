#https://www.e-olymp.com/uk/submissions/7730131

class Vertex:
    def __init__(self):
        self.mNeighbors = []
        self.mColor = None

    def addNeighbor(self, vertex):
        self.mNeighbors.append(vertex)

    def setColor(self, color):
        self.mColor = color

    def neighbors(self):
        return self.mNeighbors

    def color(self):
        return self.mColor

class Graph:
    COLORS = {"RED":"BLUE", "BLUE":"RED"}

    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = Vertex()

    def addEdge(self, source, destination):
        self[source].addNeighbor(destination)
        self[destination].addNeighbor(source)

    def __getitem__(self, item):
        return self.vertices[item]

    def isBipartite(self, vertex):
        queue = [vertex]
        self[vertex].setColor("RED")

        while queue:
            current = queue.pop(0)

            for neighbor in self[current].neighbors():
                if self[neighbor].color() == self[current].color():
                    return False
                elif self[neighbor].color() is None:
                    self[neighbor].setColor(Graph.COLORS[self[current].color()])
                    queue.append(neighbor)

        return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    ans = True

    for i in range(1, n + 1):
        if graph[i].color() is None:
            ans = graph.isBipartite(i)

        if not ans:
            break

    print("YES" if ans else "NO")
