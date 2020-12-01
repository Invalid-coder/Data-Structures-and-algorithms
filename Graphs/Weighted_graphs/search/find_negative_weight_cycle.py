import sys

INF = sys.maxsize

def BelmanFordClasical(graph, start):
    """
        For graphs with negative weight cycles
    """

    for vertex in graph:
        vertex.setDistance(INF)

    graph[start].setDistance(0)

    for i in range(len(graph) - 1):
        for vertex in graph:
            for neighbor_key in vertex.neighbors():
                neighbor = graph[neighbor_key]
                newDist = vertex.distance() + vertex.weight(neighbor_key)

                if newDist < neighbor.distance():
                    neighbor.setDistance(newDist)

    for vertex in graph:
        for neighbor_key in vertex.neighbors():
            neighbor = graph[neighbor_key]
            newDist = vertex.distance() + vertex.weight(neighbor_key)

            if newDist < neighbor.distance():
                return True

    return False
