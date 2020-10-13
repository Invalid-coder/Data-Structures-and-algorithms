#https://www.e-olymp.com/uk/submissions/7500255

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.visited = False

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def addToTail(self, item):
        node = Node(item)

        if self.empty():
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def hasCycle(self):
        node = self.head

        while not node is None:
            if node.visited:
                return 1

            node.visited = True
            node = node.next

        return 0

if __name__ == '__main__':
    p, a, b, c, m, n = map(int, input().split())
    l = LinkedList()
    x = p

    for i in range(n):
        l.addToTail(x)
        x = (a * x * x + b * x + c) % m

    k = x % n

    if x < m // 2:
        node = l.head

        for i in range(k):
            node = node.next

        l.tail.next = node
    else:
        l.tail = None

    print(l.hasCycle())