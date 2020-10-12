#https://www.e-olymp.com/uk/submissions/7498981

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class LinkedList():
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

    def reorderList(self):
        l0, ln = self.head, self.tail

        while True:
            if l0 == ln:
                l0.next = None
                self.tail = l0
                break

            if l0.next == ln:
                ln.next = None
                self.tail = ln
                break

            nextEl = l0.next
            prevEl = ln.prev

            nextEl.prev = ln
            l0.next = ln
            ln.prev = l0
            ln.next = nextEl
            l0 = nextEl
            ln = prevEl

    def __str__(self):
        s = ""
        node = self.head

        while not node is None:
            s += node.item + " "
            node = node.next

        return s

if __name__ == '__main__':
    n = int(input())
    arr = input()
    l = LinkedList(arr)
    l.reorderList()
    print(l)