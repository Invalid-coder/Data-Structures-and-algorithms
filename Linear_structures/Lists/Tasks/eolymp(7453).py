#https://www.e-olymp.com/uk/submissions/7498557

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.item)

class DoubleLinkedList():
    def __init__(self, data):
        self.head = None
        self.tail = None
        self.size = 0
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
        self.size += 1

    def rotateRight(self, k):
        k %= self.size

        if k == 0:
            return

        node = self.tail
        self.head.prev = node
        node.next = self.head
        k -= 1

        while k > 0:
            node = node.prev
            k -= 1

        node.prev.next = None
        self.tail = node.prev
        node.prev = None
        self.head = node

    def __str__(self):
        s = ""
        node = self.head

        while not node is None:
            s += node.item + " "
            node = node.next

        return s

if __name__ == '__main__':
    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            text = input.readlines()
            n = text[0].rstrip()
            arr = text[1].rstrip()
            l = DoubleLinkedList(arr)
            i = 2

            while i < len(text):
                k = int(text[i].rstrip())
                l.rotateRight(k)
                print(l, file=output)
                i += 1