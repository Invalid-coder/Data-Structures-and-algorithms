from Linear_structures.Queues.Queue.Implementation.recurcively import *
from Linear_structures.Stack.Implementation.recursively import *
from Graphs.Implementation.adjacencyList import *

def waySearch(graph, start, end):
    assert start != end

    sources = {start:None}
    queue = Queue()
    queue.enqueue(start)

    while not queue.empty():
        current = queue.dequeue()

        for neighbor in graph[current].neighbors():
            if not neighbor in sources:
                queue.enqueue(neighbor)
                sources[neighbor] = current

    if not end in sources:
        return None

    stack = Stack()
    current = end

    while not current is None:
        stack.push(current)
        current = sources[current]

    way = []

    while not stack.empty():
        way.append(stack.pop())

    return way

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

    print(waySearch(graph, 1, 5))
