#https://www.e-olymp.com/uk/submissions/7806325

import sys
sys.setrecursionlimit(10000000)

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)

    def transpose(self):
        n = len(self.vertices)
        graph_inv = Graph(n)

        for vertex in self.vertices.keys():
            for neighbor in self[vertex]:
                graph_inv.addEdge(neighbor, vertex)

        return graph_inv

    def DFS(self, start, visited, stack):
        visited.add(start)

        for neighbor in self[start]:
            if not neighbor in visited:
                self.DFS(neighbor, visited, stack)

        stack.append(start)

    def get_component(self, start, visited, component):
        visited.add(start)
        component.append(start)

        for neighbor in self[start]:
            if not neighbor in visited:
                self.get_component(neighbor, visited, component)

    def topologicalSorting(self):
        stack = []
        visited = set()

        for vertex in self.vertices.keys():
            if not vertex in visited:
                self.DFS(vertex, visited, stack)

        sequence = []

        while stack:
            sequence.append(stack.pop())

        return sequence

    def get_connected_components(self):
        counter = 0
        visited = set()
        n = len(self.vertices)
        graph_inv = self.transpose()
        sorted_list = self.topologicalSorting()
        components = [0 for i in range(n + 1)]

        for vertex in sorted_list:
            component = []

            if not vertex in visited:
                graph_inv.get_component(vertex, visited, component)
                counter += 1

                for v in component:
                    components[v] = counter

        return counter, components[1:]

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    amount, components = graph.get_connected_components()

    print(amount)
    print(*components)
