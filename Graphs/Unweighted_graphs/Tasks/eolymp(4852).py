#https://www.e-olymp.com/uk/submissions/7706428

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def DFS(self, start):
        distances = {vertex:-1 for vertex in range(len(self.adjacentMatrix))}
        distances[start] = 0

        def _DFS(graph, start, distance, visited):
            nonlocal distances

            visited.add(start)

            for neighbor, edge in enumerate(graph[start]):
                if edge == 1:
                    if not neighbor in visited:
                        if distances[neighbor] == -1:
                            distances[neighbor] = distance + 1
                        elif distances[neighbor] > distance + 1:
                            distances[neighbor] = distance + 1

                        _DFS(graph, neighbor, distance + 1, visited)

            visited.remove(start)

        _DFS(self, start, 0, set())

        return distances.values()

    def __getitem__(self, item):
        return self.adjacentMatrix[item]

if __name__ == '__main__':
    n, x = map(int, input().split())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print(*graph.DFS(x - 1))


