class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def BFS(self, start):
        inflows = []
        distances = {start:0}
        queue = [start]

        while queue:
            current = queue.pop(0)

            if len(self[current]) <= 1:
                inflows.append(current)

            for neighbor in self[current]:
                if not neighbor in distances:
                    queue.append(neighbor)
                    distances[neighbor] = distances[current] + 1

        inflow = min(inflows) if inflows else start

        return inflow, distances[inflow]

    def DFS(self, starts):
        inflow = len(self.vertices)
        dist = 0

        def _DFS(graph, start, distance, visited):
            nonlocal inflow, dist

            visited.add(start)

            if len(graph[start]) <= 1:
                if inflow == start:
                    dist = min(dist, distance)
                elif start < inflow:
                    inflow = start
                    dist = distance

            for neighbor in graph[start]:
                if not neighbor in visited:
                    _DFS(graph, neighbor, distance + 1, visited)

            visited.remove(start)

        for start in starts:
            visited = set()
            _DFS(self, start, 0, visited)

        return inflow, dist

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    k = int(input())
    starts = list(map(int, input().split()))
    inflow, dist = graph.DFS(starts)

    print(dist)
    print(inflow)