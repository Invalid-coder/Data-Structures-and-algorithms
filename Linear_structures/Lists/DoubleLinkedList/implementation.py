class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self):
        self.first = None
        self.last = None
        self.curr = None

    def empty(self):
        return self.first is None

    def setFirst(self):
        self.curr = self.first

    def setLast(self):
        self.curr = self.last

    def next(self):
        if self.curr != self.last:
            self.curr = self.curr.next

    def prev(self):
        if self.curr != self.first:
            self.curr = self.curr.prev

    def current(self):
        if self.empty():
            return None
        else:
            return self.curr.item

    def insertBefore(self, item):
        node = Node(item)
        node.next = self.curr

        if self.empty():
            self.first = self.last = self.curr = node
        else:
            if self.curr == self.first:
                self.first = node
            else:
                node.prev = self.curr.prev
                self.curr.prev.next = node

            self.curr.prev = node

    def insertAfter(self, item):
        node = Node(item)
        node.prev = self.curr

        if self.empty():
            self.first = self.last = self.curr = node
        else:
            if self.curr == self.last:
                self.last = node
            else:
                node.next = self.curr.next
                self.curr.next.prev = node

            self.curr.next = node
            self.curr = node

    def remove(self):
        if self.empty():
            raise Exception("DoubleLinkedList: 'remove' applied to an empty container")

        node = self.curr

        if node == self.first:
            self.first = node.next
        else:
            node.prev.next = node.next

        if node == self.last:
            self.curr = self.last = node.prev
        else:
            node.next.prev = node.prev
            self.curr = node.next

        del node
