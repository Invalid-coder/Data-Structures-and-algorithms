from Graphs.Implementation.adjacencyList import *

def DFS(graph, start, visited, stack):
    visited.add(start)

    for neighbor in graph[start].neighbors():
        if not neighbor in visited:
            DFS(graph, neighbor, visited, stack)

    stack.append(start)

def topological_sorting(graph):
    stack = []
    visited = set()

    for vertex in graph.mVertices.keys():
        if not vertex in visited:
            DFS(graph, vertex, visited, stack)

    sequence = []

    while stack:
        sequence.append(stack.pop())

    return sequence

def get_component(graph, start, visited, connected_component):
    visited[start] = connected_component

    for neighbor in graph[start].neighbors():
        if not neighbor in visited:
            get_component(graph, neighbor, visited, connected_component)

def get_strong_connected_components(graph):
    assert graph.isOriented

    counter = 0
    visited = {}
    graph_inv = graph.transpose()
    sorted_list = topological_sorting(graph)

    for vertex in sorted_list:
        component = []

        if not vertex in visited:
            counter += 1
            get_component(graph_inv, visited, vertex, counter)

    print(visited)

    return counter

if __name__ == '__main__':
    graph = Graph(True)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 1)
    graph.addEdge(4, 5)
    graph.addEdge(5, 6)
    graph.addEdge(6, 4)
    graph.addEdge(2, 4)
    print(get_strong_connected_components(graph))