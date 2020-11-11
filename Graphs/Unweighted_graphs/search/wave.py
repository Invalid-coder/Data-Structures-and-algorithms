from Linear_structures.Queues.Queue.Implementation.recurcively import *
from Graphs.Implementation.adjacencyList import *

def wave(graph, start):
    queue = Queue()
    queue.enqueue(start)
    distances = {start:0}

    while not queue.empty():
        current = queue.dequeue()

        for neighbor in graph[current].neighbors():
            if not neighbor in distances:
                queue.enqueue(neighbor)
                distances[neighbor] = distances[current] + 1

    return distances

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

    print(wave(graph, 1))