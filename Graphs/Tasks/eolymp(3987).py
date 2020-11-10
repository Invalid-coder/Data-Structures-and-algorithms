#https://www.e-olymp.com/uk/submissions/7686272

class Graph:
    def __init__(self, n):
        self.adjacentMatrix = []

        for i in range(n):
            self.adjacentMatrix.append([0] * n)

    def addEdge(self, source, destination):

        self.adjacentMatrix[source][destination] = 1
        self.adjacentMatrix[destination][source] = 1

    def isFullGraph(self):
        n = len(self.adjacentMatrix)

        for i in range(n):
            for j in range(i + 1, n):
                if self.adjacentMatrix[i][j] == 0:
                    return False

        return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for i in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source - 1, destination - 1)

    print("YES" if graph.isFullGraph() else "NO")