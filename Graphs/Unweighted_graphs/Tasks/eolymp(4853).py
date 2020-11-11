#https://www.e-olymp.com/uk/submissions/7694906

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def waySearch(self, start, end):
        sources = {start:None}
        queue = [start]

        while queue:
            current = queue.pop(0)

            if current == end:
                break

            for neighbor in self[current]:
                if not neighbor in sources:
                    queue.append(neighbor)
                    sources[neighbor] = current

        if not end in sources:
            return None

        stack = []
        current = end

        while not current is None:
            stack.append(current)
            current = sources[current]

        way = []

        while stack:
            way.append(stack.pop())

        return way

    def __getitem__(self, vertex):
        return self.vertices[vertex]

if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    res = graph.waySearch(a, b)

    if res:
        print(len(res) - 1)
        print(*res)
    else:
        print(-1)