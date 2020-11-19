class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def get_connected_components(self):
        remaining = set(self.vertices.keys())
        components = []
        stack = [remaining.pop()]
        component = set()

        while remaining:
            if stack:
                current = stack.pop()
                component.add(current)
            else:
                current = remaining.pop()
                components.append(component)
                component = {current}

            for neighbor in self[current]:
                if neighbor in remaining:
                    stack.append(neighbor)
                    remaining.remove(neighbor)

        while stack:
            component.add(stack.pop())

        if component:
            components.append(component)

        return components

    """
    #Second option implemented with using dfs search
    
    def dfs(self, start, visited, component):
        visited.add(start)
        component.add(start)

        for neighbor in self[start]:
            if not neighbor in visited:
                self.dfs(neighbor, visited, component)

    def get_connected_components(self):
        components = []
        visited = set()

        for key in self.vertices.keys():
            component = set()

            if not key in visited:
                self.dfs(key, visited, component)
                components.append(component)

        return components
    """

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    connected_components = graph.connected_components()
    print(len(connected_components))

    for component in connected_components:
        print(len(component))
        print(*component)
