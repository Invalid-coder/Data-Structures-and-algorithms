from Graphs.Implementation.connectivity import _check_connectivity_helper
from Graphs.Implementation.adjacencyList import *

"""
Checking strong connectivity for oriented graph
"""

def checkStrongConnectivity(graph):
    assert graph.isOriented

    if not _check_connectivity_helper(graph, 1):# start can be any vertex that the graph contains
        return False

    graph_inv = graph.transpose()

    return  _check_connectivity_helper(graph_inv, 1)# start can be any vertex that the graph contains

def test():
    g = Graph(True)
    g.addEdge(1, 4)
    g.addEdge(1, 7)
    g.addEdge(4, 7)

    print("Graph is strong connected: ", checkStrongConnectivity(g))

if __name__ == '__main__':
    test()
