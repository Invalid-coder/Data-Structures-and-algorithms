class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.curr = None

    def empty(self):
        return self.curr is None

    def next(self):
        if self.empty():
            raise StopIteration
        else:
            self.curr = self.curr.next

    def current(self):
        if self.empty():
            return None
        else:
            return self.curr.item

    def insert(self, item):
        node = Node(item)

        if self.empty():
            node.next = node
            self.curr = node
        else:
            node.next = self.curr.next
            self.curr.next = node

