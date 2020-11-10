#https://www.e-olymp.com/uk/submissions/7687323

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def get_vertices_degree(self):
        degrees = []
        n = len(self.adjacentMatrix)

        for i in range(n):
            counter = 0

            for j in range(n):
                if self.adjacentMatrix[i][j] == 1:
                    counter += 1

            degrees.append(counter)

        return degrees

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print(*graph.get_vertices_degree())
