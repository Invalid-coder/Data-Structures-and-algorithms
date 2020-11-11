#https://www.e-olymp.com/uk/submissions/7687618

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def isNotOriented(self):
        n = len(self.adjacentMatrix)

        for i in range(n):
            for j in range(n):
                if i == j and self.adjacentMatrix[i][j] == 1:
                    return False
                if self.adjacentMatrix[i][j] != self.adjacentMatrix[j][i]:
                    return False

        return True

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print("YES" if graph.isNotOriented() else "NO")

