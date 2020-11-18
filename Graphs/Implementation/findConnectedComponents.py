from Graphs.Implementation.adjacencyList import *

def DFS(graph, visited, start, connected_component):
    visited[start] = connected_component

    for neighbor in graph[start].neighbors():
        if not neighbor in visited:
            DFS(graph, visited, neighbor, connected_component)

def findConnectedComponents(graph):
    assert not graph.isOriented

    visited = {}
    connected_component = 0

    for v in graph.vertices():
        if not v in visited:
            connected_component += 1
            DFS(graph, visited, v, connected_component)

    print(visited)

    return connected_component

if __name__ == '__main__':
    g = Graph()
    #First connected component
    g.addEdge(1, 4)
    g.addEdge(1, 7)
    g.addEdge(4, 7)
    # Second connected component
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(3, 5)
    g.addEdge(3, 6)
    g.addEdge(5, 6)
    print("Amount of connected components: ", findConnectedComponents(g))