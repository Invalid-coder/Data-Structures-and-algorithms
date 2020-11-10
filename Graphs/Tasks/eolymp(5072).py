#https://www.e-olymp.com/uk/submissions/7685314

class Graph:
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix

    def get_count_of_edges(self):
        counter = 0
        n = len(self.matrix)

        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    counter += 1

        return counter


if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    graph = Graph(matrix)
    print(graph.get_count_of_edges())