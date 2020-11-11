#https://www.e-olymp.com/uk/submissions/7688555

class Graph:
    def __init__(self, n):
        self.adjacentMatrix = []

        for i in range(n):
            self.adjacentMatrix.append([0] * n)

    def addEdge(self, source, destination):
        self.adjacentMatrix[source][destination] = 1

    def isHalfFull(self):
        n = len(self.adjacentMatrix)

        for i in range(n):
            for j in range(n):
                if i != j:
                    if self.adjacentMatrix[i][j] == 0 and self.adjacentMatrix[j][i] == 0:
                        return False

        return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source - 1, destination - 1)

    print("YES" if graph.isHalfFull() else "NO")