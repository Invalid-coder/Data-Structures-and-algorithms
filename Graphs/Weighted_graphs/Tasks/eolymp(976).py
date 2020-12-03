import sys
INF = sys.maxsize

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def Dijkstra(self, start):
        N = len(self.adjacentMatrix)
        distances = [INF] * N
        exists = [0] * N
        fixed = [False] * N
        distances[start] = 0

        while True:
            current = start
            fixed[current] = True

            for neighbor, edge in enumerate(self[current]):
                if fixed[neighbor]:
                    if edge < 0:
                        exists[neighbor] = 2
                        exists[current] = 2
                    elif edge > 0:
                        exists[neighbor] = 1

                    continue

                if edge != 0:
                    newDist = distances[current] + edge

                    if newDist < distances[neighbor]:
                        distances[neighbor] = newDist

                    exists[neighbor] = 1

            distance = INF

            for neighbor, edge in enumerate(self[current]):
                if not fixed[neighbor] and distances[neighbor] < distance:
                    start = neighbor
                    distance = distances[neighbor]

            if distance == INF:
                break

        return exists

    def find_matrix_way(self):
        N = len(self.adjacentMatrix)
        matrix = []

        for start in range(N):
            distances = self.Dijkstra(start)
            matrix.append(distances)

        return matrix

    def __getitem__(self, item):
        return self.adjacentMatrix[item]

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    matrix = graph.find_matrix_way()

    for row in matrix:
        print(*row)