#https://www.e-olymp.com/uk/submissions/7685469

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def get_count_of_hanging_vertices(self):
        n = len(self.adjacentMatrix)
        counter = 0

        for i in range(n):
            neighbors = 0

            for j in range(n):
                if self.adjacentMatrix[i][j] == 1:
                    neighbors += 1

            if neighbors == 1:
                counter += 1

        return counter

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    graph = Graph(matrix)
    print(graph.get_count_of_hanging_vertices())