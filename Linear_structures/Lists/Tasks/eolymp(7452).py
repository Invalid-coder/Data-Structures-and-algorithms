#https://www.e-olymp.com/uk/submissions/7498009

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self, data):
        self.head = None
        self.tail = None
        self.initList(data)

    def initList(self, data):
        for item in data.split():
            self.addToTail(item)

    def empty(self):
        return self.head is None

    def addToTail(self, item):
        node = Node(item)
        node.prev = self.tail

        if self.empty():
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def print(self):
        s = ""
        node = self.head

        while not node is None:
            s += node.item + " "
            node = node.next

        print(s)

    def printReverse(self):
        s = ""
        node = self.tail

        while not node is None:
            s += node.item + " "
            node = node.prev

        print(s)

if __name__ == '__main__':
    n = int(input())
    l = DoubleLinkedList(input())
    l.print()
    l.printReverse()