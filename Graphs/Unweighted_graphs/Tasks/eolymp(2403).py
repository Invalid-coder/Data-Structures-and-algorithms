#https://www.e-olymp.com/uk/submissions/7806456

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

    def get_component(self, start, visited):
        visited.add(start)

        for neighbor in self[start]:
            if not neighbor in visited:
                self.get_component(neighbor, visited)

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

    def get_components_amount(self):
        counter = 0
        visited = set()
        graph_inv = self.transpose()
        sorted_list = self.topologicalSorting()

        for vertex in sorted_list:
            if not vertex in visited:
                graph_inv.get_component(vertex, visited)
                counter += 1

        return counter

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    amount = graph.get_components_amount()

    print(amount)