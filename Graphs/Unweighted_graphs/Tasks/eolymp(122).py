#https://www.e-olymp.com/uk/submissions/7702956

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self.vertices[source].append(destination)

    def DFS(self, start, end, days):
        ways = 0
        visited = set()

        def _DFS(graph, curr_day, end_day, start, end, visited):
            nonlocal ways

            if curr_day >= end_day:
                return

            visited.add(start)

            for neighbor in graph[start]:
                if not neighbor in visited:
                    if neighbor == end:
                        ways += 1

                    _DFS(graph, curr_day + 1, end_day, neighbor, end, visited)

            visited.remove(start)

        _DFS(self, 0, days, start, end, visited)

        return ways

    def __getitem__(self, vertex):
        return self.vertices[vertex]

if __name__ == '__main__':
    n, k, a, b, d = map(int, input().split())
    graph = Graph(n)

    for i in range(k):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    print(graph.DFS(a, b, d))