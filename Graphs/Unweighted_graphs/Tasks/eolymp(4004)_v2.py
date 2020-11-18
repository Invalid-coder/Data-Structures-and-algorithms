#https://www.e-olymp.com/uk/submissions/7756801

WHITE = 0
GRAY = 1
BLACK = 2

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def DFS(self, start, colors):
        if colors[start] == BLACK:
            return

        if colors[start] == GRAY:
            raise Exception

        for neighbor, edge in enumerate(self.adjacentMatrix[start]):
            if edge == 1:
                self.DFS(neighbor, colors)

        colors[start] = BLACK

    def hasCycle(self):
        n = len(self.adjacentMatrix)
        vertex_colors = [WHITE for _ in range(n)]

        try:
            for vertex in range(n):
                self.DFS(vertex, vertex_colors)
        except Exception:
            return True

        return False

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print(int(graph.hasCycle()))