class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList():
    def __init__(self):
        self.first = None

    def empty(self):
        return self.first is None

    def insert(self, item):
        node = Node(item)
        node.next = self.first
        self.first = node

    def head(self):
        if self.empty():
            return None
        else:
            return self.first.item

    def tail(self):
        if self.empty():
            raise Exception("LinkedList: 'tail' applied to an empty container")
        else:
            self.first = self.first.next
            return self