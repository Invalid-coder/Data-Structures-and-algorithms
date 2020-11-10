#https://www.e-olymp.com/uk/submissions/7688910

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def isTransitive(self):
        n = len(self.adjacentMatrix)

        for u in range(n):
            for v in range(n):
                if u != v:
                    for w in range(n):
                        if w != u and w != v:
                            if self.adjacentMatrix[u][v] == 1:
                                if self.adjacentMatrix[v][w] == 1:
                                    if self.adjacentMatrix[u][w] == 0:
                                        return False

        return True

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print("YES" if graph.isTransitive() else "NO")

