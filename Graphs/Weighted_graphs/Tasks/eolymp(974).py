#BelmanFord
#https://www.e-olymp.com/uk/submissions/7906086
#Dijkstra
#https://www.e-olymp.com/uk/submissions/7906261

INF = 100

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def BelmanFord(self, start):
        N = len(self.adjacentMatrix)
        distances = [INF] * N
        distances[start] = 0

        for _ in range(N - 1):
            for i in range(N):
                for neighbor, edge in enumerate(self[i]):
                    if edge != 0:
                        newDist = distances[i] + edge

                        if newDist < distances[neighbor]:
                            distances[neighbor] = newDist

        return distances

    def Dijkstra(self, start):
        N = len(self.adjacentMatrix)
        distances = [INF] * N
        fixed = [False] * N
        distances[start] = 0

        while True:
            current = start
            fixed[current] = True

            for neighbor, edge in enumerate(self[current]):
                if fixed[neighbor]:
                    continue

                if edge != 0 and edge != INF:
                    newDist = distances[current] + edge

                    if newDist < distances[neighbor]:
                        distances[neighbor] = newDist

            distance = INF

            for neighbor, edge in enumerate(self[current]):
                if not fixed[neighbor] and distances[neighbor] < distance:
                    start = neighbor
                    distance = distances[neighbor]

            if distance == INF:
                break

        return distances

    def find_matrix_way(self):
        N = len(self.adjacentMatrix)
        matrix = []

        for start in range(N):
            distances = self.Dijkstra(start)#self.BelmanFord(start)
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
