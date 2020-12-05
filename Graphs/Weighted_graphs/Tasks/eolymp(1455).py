import sys

INF = sys.maxsize

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def __getitem__(self, item):
        return self.adjacentMatrix[item]

    def __len__(self):
        return len(self.adjacentMatrix)

def BelmanFord(graph, start):
    distances = [INF] * len(graph)
    sources = [None] * len(graph)
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in range(len(graph)):
            for neighbor, edge in enumerate(graph[vertex]):
                if edge != 0:
                    newDist = distances[vertex] + edge

                    if newDist < distances[neighbor]:
                        distances[neighbor] = newDist
                        sources[neighbor] = vertex

    for vertex in range(len(graph)):
        for neighbor, edge in enumerate(graph[vertex]):
            if edge != 0:
                newDist = distances[vertex] + edge

                if newDist < distances[neighbor]:
                    return vertex, sources

    return None

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    ans = BelmanFord(graph, 0)

    if not ans is None:
        print("YES")
        vertex, sources = ans
        stack = []

        while True:
            if vertex + 1 in stack:
                stack.append(vertex + 1)
                break

            stack.append(vertex + 1)
            vertex = sources[vertex]

        print(len(stack))

        while stack:
            print(stack.pop(), end=' ')
    else:
        print("NO")
