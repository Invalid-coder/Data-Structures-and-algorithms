#https://www.e-olymp.com/uk/submissions/7692873

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def wave(self, start, end):
        queue = [start]
        distances = {start:0}

        while len(queue) > 0:
            current = queue.pop(0)

            if current == end:
                return distances[current]

            for neighbor, edge in enumerate(self.adjacentMatrix[current]):
                if edge == 1 and not neighbor in distances:
                    queue.append(neighbor)
                    distances[neighbor] = distances[current] + 1

        return 0

if __name__ == '__main__':
    n, s, f = map(int, input().split())
    matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print(graph.wave(s - 1, f - 1))