from Linear_structures.Queues.Queue.Implementation.recurcively import *
from Trees.RegularTree.implementation import *

def BFS(root):
    queue= Queue()
    queue.enqueue(root)

    while not queue.empty():
        node = queue.dequeue()
        print(node.key(), end="->")

        for child in node.getChildren():
            queue.enqueue(child)

def search(root, key):
    queue = Queue()
    queue.enqueue(root)

    while not queue.empty():
        node = queue.dequeue()

        if node.key() == key:
            return True

        for child in node.getChildren():
            queue.enqueue(child)

    return False

if __name__ == '__main__':
    tree = createSampleTree()
    BFS(tree)
    print()
    print(search(tree, 15))
