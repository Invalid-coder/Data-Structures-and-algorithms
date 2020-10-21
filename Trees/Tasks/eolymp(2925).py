class Vertex():
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=1):
        self.neighbors[vertex] = weight

    def neighbor(self, neighbor):
        return self.neighbors[neighbor]

    def weight(self, neighbor):
        return self.neighbors[neighbor]

    def getNeighbors(self):
        return self.neighbors.keys()

class Graph():
    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertex):
        new_vertex = Vertex(vertex)
        self.vertices[vertex] = new_vertex

    def getVertices(self):
        return self.vertices

    def getVertex(self, vertex):
        return self.vertices[vertex]

    def addEdge(self, source, destination, weight):
        if source not in self:
            self.addVertex(source)
        if destination not in self:
            self.addVertex(destination)

        self[source].addNeighbor(destination, weight)
        self[destination].addNeighbor(source, weight)

    def __contains__(self, item):
        return item in self.vertices

    def __getitem__(self, item):
        return self.getVertex(item)

finish = False

def DFS(graph, visited, start, curr):
    global finish

    visited.add(start)

    if len(curr) == len(s):
        if curr == s:
            print('YES')
            print('{} {}'.format(v, start))
            finish = True

        return

    if curr != s[:len(curr)]:
        return

    for neighbor in graph[start].getNeighbors():
        if not neighbor in visited:
            DFS(graph, visited, neighbor, curr + graph[start].weight(neighbor))

if __name__ == '__main__':
    s = input()
    n = int(input())
    graph = Graph()
    starts = set()

    for i in range(n - 1):
        a,b,w = input().split()
        a, b = int(a), int(b)
        graph.addEdge(a, b, w)
        graph.addEdge(b, a, w)

        if w == s[0]:
            starts.add(a)
            starts.add(b)

    for v in starts:
        if not finish:
            visited = set()
            DFS(graph, visited, v, '')
        else:
            break

    if not finish:
        print('NO')
