#https://www.e-olymp.com/uk/submissions/7484604

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque():
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None and self.back is None

    def pushfront(self, item):
        node = Node(item)
        node.next = self.front

        if self.empty():
            self.back = node
        else:
            self.front.prev = node

        self.front = node

    def popfront(self):
        front = self.front
        item = front.item
        self.front = self.front.next
        del front

        if self.front is None:
            self.back = None
        else:
            self.front.prev = None

        return item

    def pushback(self, item):
        node = Node(item)
        node.prev = self.back

        if self.empty():
            self.front = node
        else:
            self.back.next = node

        self.back = node

    def popback(self):
        back = self.back
        item = back.item
        self.back = self.back.prev
        del back

        if self.back is None:
            self.front = None
        else:
            self.back.next = None

        return item

    def execute(self, command):
        name = command[0]
        args = command[1:]

        return getattr(self, name)(*args)


if __name__ == '__main__':
    n = int(input())
    deques = {}

    for i in range(n):
        line = input().split()
        d = line.pop(1)

        if d not in deques:
            deques[d] = Deque()

        res = deques[d].execute(line)

        if res:
            print(res)

