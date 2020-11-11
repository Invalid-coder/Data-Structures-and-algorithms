from Graphs.Implementation.adjacencyList import *

def DFS(graph, start):
    visited = set()
    __dfs_helper(graph, start, visited)
    return visited

def __dfs_helper(graph, start, visited):
    visited.add(start)

    print(start, end="->")

    for neighbor in graph[start].neighbors():
        if not neighbor in visited:
            __dfs_helper(graph, neighbor, visited)

if __name__ == '__main__':
    graph = Graph(True)

    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(2, 5)
    graph.addEdge(3, 5)
    graph.addEdge(3, 6)
    graph.addEdge(4, 3)
    graph.addEdge(4, 6)
    graph.addEdge(5, 4)
    graph.addEdge(5, 6)

    DFS(graph, 1)
    print()
    DFS(graph, 5)
    print()
    DFS(graph, 4)
    print()
    DFS(graph, 2)
