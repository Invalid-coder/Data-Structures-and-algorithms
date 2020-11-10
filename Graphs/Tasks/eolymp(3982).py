#https://www.e-olymp.com/uk/submissions/7684125

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key, neighbors):
        self.vertices[key] = neighbors

    def get_adjacency_matrix(self):
        matrix = []
        n = len(self.vertices)

        for i in range(1, n + 1):
            matrix.append([0] * n)

            for j in self.vertices[i]:
                matrix[i - 1][j - 1] = 1

        return matrix

if __name__ == '__main__':
    n = int(input())
    graph = Graph()

    for i in range(1, n + 1):
        neighbors = list(map(int, input().split()))[1:]
        graph.addVertex(i, neighbors)

    for row in graph.get_adjacency_matrix():
        print(*row)
