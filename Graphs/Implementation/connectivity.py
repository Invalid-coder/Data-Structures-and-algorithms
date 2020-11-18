from Graphs.Implementation.adjacencyList import *
from Graphs.Unweighted_graphs.search.DFS import *
"""
Checking connectivity for not oriented graph
"""

def _check_connectivity_helper(graph, start):
    visited = DFS(graph, start)

    for vertex in graph.vertices():
        if not vertex in visited:
            return False

    return True

def check_connectivity(graph):
    assert not graph.isOriented

    return _check_connectivity_helper(graph, 1) # start can be any vertex that the graph contains

def test1():
    g = Graph()
    # First connected component
    g.addEdge(1, 4)
    g.addEdge(1, 7)
    g.addEdge(4, 7)
    # Second connected component
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(3, 5)
    g.addEdge(3, 6)
    g.addEdge(5, 6)

    print("Graph is connected: ", check_connectivity(g))

def test2():
    g = Graph()
    g.addEdge(1, 4)
    g.addEdge(1, 7)
    g.addEdge(4, 7)

    print("Graph is connected: ", check_connectivity(g))

if __name__ == '__main__':
    test1()
    test2()