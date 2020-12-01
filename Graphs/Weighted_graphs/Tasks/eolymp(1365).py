#https://www.e-olymp.com/uk/submissions/7900599

import sys

INF = sys.maxsize

class Vertex:
    def  __init__(self):
        self.mDistance = INF
        self.mNeighbors = {}

    def distance(self):
        return self.mDistance

    def neighbors(self):
        return self.mNeighbors

    def setDistance(self, distance):
        self.mDistance = distance

    def addNeighbor(self, neighbor, weight):
        self.mNeighbors[neighbor] = weight

class Graph:
    def __init__(self, matrix):
       self.adjacentMatrix = matrix

    def Dijkstra(self, start):
        distances = [INF] * len(self)
        visited = [False] * len(self)
        distances[start] = 0

        while True:
            current = start
            visited[current] = True

            for neighbor, edge in enumerate(self[current]):
                if edge != -1 and edge != 0:
                    newDist = distances[current] + self.weight(current, neighbor)

                    if newDist < distances[neighbor]:
                        distances[neighbor] = newDist

            distance = INF

            for neighbor, edge in enumerate(self[current]):
                if not visited[neighbor] and distances[neighbor] < distance:
                    distance = distances[neighbor]
                    start = neighbor

            if distance == INF:
                break

        return distances

    def weight(self, source, destination):
        return self.adjacentMatrix[source][destination]

    def __len__(self):
        return len(self.adjacentMatrix)

    def __getitem__(self, item):
        return self.adjacentMatrix[item]

if __name__ == '__main__':
    n, s, f = map(int, input().split())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    distances = graph.Dijkstra(s - 1)

    if distances[f - 1] != INF:
        print(distances[f - 1])
    else:
        print(-1)
