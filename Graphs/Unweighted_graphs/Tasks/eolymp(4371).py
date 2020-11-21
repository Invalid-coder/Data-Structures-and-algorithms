class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def dfs(self, start, visited):
        visited.add(start)

        for neighbor in self[start]:
            if not neighbor in visited:
                self.dfs(neighbor, visited)

    def get_components_amount(self, visited):
        counter = 0

        for key in self.vertices.keys():
            if not key in visited:
                counter += 1
                self.dfs(key, visited)

        return counter

    def bfs(self, start):
        ans = [self.get_components_amount(set())]
        visited = {start}
        queue = [start]
        t = 0

        while True:
            ans.append(self.get_components_amount(visited.copy()))
            temp = []
            t += 1

            while queue:
                current = queue.pop(0)

                for neighbor in self[current]:
                    if not neighbor in visited:
                        visited.add(neighbor)
                        temp.append(neighbor)

            if not temp:
                break

            queue = temp.copy()

        return t, ans

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    t, ans = graph.bfs(s)
    print(t)
    print(*ans)
