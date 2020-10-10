#https://www.e-olymp.com/uk/submissions/7483353

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None and self.back is None

    def append(self, item):
        node = Node(item)

        if self.empty():
            self.front = node
        else:
            self.back.next = node

        self.back = node

    def pop(self):
        front = self.front
        item = front.item
        self.front = self.front.next
        del front

        if self.front is None:
            self.back = None

        return item

if __name__ == '__main__':
    N, k = map(int, input().split())
    queue = Queue()

    for i in range(1, N + 1):
        queue.append(i)

    current = None

    while not queue.empty():
        for i in range(k - 1):
            queue.append(queue.pop())

        current = queue.pop()

    print(current)