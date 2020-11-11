from Linear_structures.Queues.Queue.Implementation.recurcively import *
from Graphs.Implementation.adjacencyList import *

def BFS(graph, start):
    visited = set()
    queue = Queue()
    queue.enqueue(start)
    visited.add(start)

    while not queue.empty():
        current = queue.dequeue()

        print(current, end="->")

        for neighbor in graph[current].neighbors():
            if not neighbor in visited:
                queue.enqueue(neighbor)
                visited.add(neighbor)

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

    BFS(graph, 1)
    print()
    BFS(graph, 5)
    print()
    BFS(graph, 4)
    print()
    BFS(graph, 2)