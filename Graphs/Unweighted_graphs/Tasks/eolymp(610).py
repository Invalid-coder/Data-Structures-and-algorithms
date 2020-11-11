#https://www.e-olymp.com/uk/submissions/7688688

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def get_count_of_edges(self):
        n = len(self.adjacentMatrix)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                if self.adjacentMatrix[i][j] == 1:
                    counter += 1

        return counter

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print(graph.get_count_of_edges())