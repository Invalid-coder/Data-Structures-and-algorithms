#https://www.e-olymp.com/uk/submissions/7906638

import sys

INF = sys.maxsize

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

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

                if edge != 0 and edge != -1:
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

        max_value = 0

        for value in distances:
            if value != INF:
                max_value = max(value, max_value)

        return max_value

    def find_max_shortest_distance(self):
        N = len(self.adjacentMatrix)
        max_dist = 0

        for start in range(N):
            distance = self.Dijkstra(start)
            max_dist = max(max_dist, distance)

        return max_dist

    def __getitem__(self, item):
        return self.adjacentMatrix[item]

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    distance = graph.find_max_shortest_distance()

    print(distance)