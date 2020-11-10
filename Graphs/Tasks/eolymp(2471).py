#https://www.e-olymp.com/uk/submissions/7683930

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def get_list_of_edges(self):
        vertices = []
        n = len(self.adjacentMatrix)

        for i in range(n):
            neighbors = []

            for j in range(i + 1, n):
                if self.adjacentMatrix[i][j] == 1:
                    neighbors.append(j)

            vertices.append(neighbors)

        return vertices

if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for i in range(n)]
    graph = Graph(matrix)
    vertices = graph.get_list_of_edges()

    for i in range(n):
        for j in vertices[i]:
            print(i + 1, j + 1)