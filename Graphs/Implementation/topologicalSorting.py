from Graphs.Implementation.vertex import *
from Graphs.Implementation.adjacencyList import *

WHITE = 0 # for unprocessed vertices
GRAY = 1  # for processing vertices
BLACK = 2 # for processed vertices

class ColorVertex(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.mColor = WHITE

    def setColor(self, color):
        self.mColor = color

    def color(self):
        return self.mColor

class ColorGraph(Graph):
    def addVertex(self, vertex):
        if vertex in self:
            return False

        new_vertex = ColorVertex(vertex)
        self.mVertices[vertex] = new_vertex
        self.vertexNumber += 1

        return True

def DFS(graph, vertex, stack):
    if vertex.color() == BLACK:
        return

    if vertex.color() == GRAY:
        raise Exception("Here is a cycle")

    vertex.setColor(GRAY)

    for neighbor_key in graph[vertex].neighbors():
        neighbor = graph[neighbor_key]
        DFS(graph, neighbor, stack)

    vertex.setColor(BLACK)
    stack.append(vertex.key())

def topological_sorting(graph):
    stack = []

    for vertex in graph:
        DFS(graph, vertex, stack)

    sequence = []

    while stack:
        sequence.append(stack.pop())

    return sequence

if __name__ == '__main__':
    g = ColorGraph(True) # creating oriented graph
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(3, 6)
    g.addEdge(4, 6)
    g.addEdge(5, 4)
    g.addEdge(5, 6)
    s = topological_sorting(g)
    print(*s)



