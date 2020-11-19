#https://www.e-olymp.com/uk/submissions/7769916

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def get_components_amount(self):
        remaining = set(self.vertices.keys())
        stack = []
        counter = 0

        while remaining:
            if stack:
                current = stack.pop()
            else:
                current = remaining.pop()
                counter += 1

            for neighbor in self[current]:
                if neighbor in remaining:
                    stack.append(neighbor)
                    remaining.remove(neighbor)

        return counter

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    print(graph.get_components_amount())