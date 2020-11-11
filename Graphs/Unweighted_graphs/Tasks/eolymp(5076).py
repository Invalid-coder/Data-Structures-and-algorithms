#https://www.e-olymp.com/uk/submissions/7688337

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self.vertices[source].append(destination)
        self.vertices[destination].append(source)

    def isRegular(self):
        firstDegree = len(self.vertices[1])
        n = len(self.vertices)

        for i in range(2, n + 1):
            currDegree = len(self.vertices[i])

            if firstDegree != currDegree:
                return False

        return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    print("YES" if graph.isRegular() else "NO")
