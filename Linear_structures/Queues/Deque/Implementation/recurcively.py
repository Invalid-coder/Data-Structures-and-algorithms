class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None and self.back is None

    def appendLeft(self, item):
        node = Node(item)
        node.next = self.front

        if self.empty():
            self.back = node
        else:
            self.front.prev = node

        self.front = node

    def popLeft(self):
        if self.empty():
            raise Exception("Deque: 'popLeft' applied to an empty container")

        current_front = self.front
        item = current_front.item
        self.front = self.front.next
        del current_front

        if self.front is None:
            self.back = None
        else:
            self.front.prev = None

        return item

    def append(self, item):
        node = Node(item)
        node.prev = self.back

        if self.empty():
            self.front = node
        else:
            self.back.next = node

        self.back = node

    def pop(self):
        if self.empty():
            raise Exception("Deque: 'pop' applied to an empty container")

        current_back = self.back
        item = current_back.item
        self.back = self.back.prev
        del current_back

        if self.back is None:
            self.front = None
        else:
            self.back.next = None

        return item

    def __del__(self):
        while not self.front is None:
            front = self.front
            self.front = self.front.next
            del front

        self.back = None

