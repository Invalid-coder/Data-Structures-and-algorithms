class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.currentSize = 0

    def empty(self):
        return self.front is None and self.back is None

    def enqueue(self, item):
        node = Node(item)

        if self.empty():
            self.front = node
        else:
            self.back.next = node

        self.back = node
        self.currentSize += 1

    def dequeue(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to an empty container")

        current_front = self.front
        item = current_front.item
        self.front = self.front.next
        self.currentSize -= 1
        del current_front

        if self.front is None:
            self.back = None

        return item
