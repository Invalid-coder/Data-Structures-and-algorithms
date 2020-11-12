#https://www.e-olymp.com/uk/submissions/7104250

class Graph():
    def __init__(self, n):
        self.n = n
        self.adjacentMatrix = []
        self.initGraph(n)

    def initGraph(self, n):
        for i in range(n):
            self.adjacentMatrix.append([0] * n)

    def addEdge(self, source, destination, weight=1):
        self.adjacentMatrix[source][destination] = weight
        self.adjacentMatrix[destination][source] = weight

    def edgeExists(self, source, destination):
        return bool(self.adjacentMatrix[source][destination])

    def DFS(self):
        visited = [False for i in range(self.n)]
        self.DFS_helper(0, 0, visited)

    def DFS_helper(self, curr, previous, visited):
        visited[curr] = True

        for next in range(self.n):
            if self.edgeExists(curr, next):
                if not visited[next]:
                    self.DFS_helper(next, curr, visited)
                else:
                    if previous != next:
                        self.adjacentMatrix[next][curr] = 0
                        self.adjacentMatrix[curr][next] = 0

        visited[curr] = False

    def printEdges(self):
        for i in range(self.n):
            for j in range(i, self.n):
                if self.edgeExists(i, j):
                    print('{} {}'.format(i + 1, j + 1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for i in range(m):
        x, y = map(int, input().split())
        graph.addEdge(x - 1, y - 1)

    for row in graph.adjacentMatrix:
        print(*row)

    graph.DFS()
    graph.printEdges()
