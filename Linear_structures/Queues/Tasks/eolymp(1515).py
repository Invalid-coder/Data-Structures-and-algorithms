#https://www.e-olymp.com/uk/submissions/7484775

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def empty(self):
        return self.front is None and self.back is None

    def append(self, item):
        node = Node(item)

        if self.empty():
            self.front = node
        else:
            self.back.next = node

        self.back = node
        self.size += 1

    def pop(self):
        front = self.front
        item = front.item
        self.front = self.front.next
        self.size -= 1
        del front

        if self.front is None:
            self.back = None

        return item

    def __str__(self):
        s = ""
        node = self.front

        while not node is None:
            s += " " + str(node.item)
            node = node.next

        return s

    def __len__(self):
        return self.size

if __name__ == '__main__':
    k = int(input())
    queue = Queue()

    for i in range(1, k + 1):
        n = int(input())
        k = 0
        j = 0

        while True:
            for l in range(1, n + 1):
                queue.append(l)

            while len(queue) > 1:
                queue.append(queue.pop())
                queue.pop()

            k = queue.pop()

            if k == n:
                break
            else:
                n = k

            j += 1

        print("Case {}: {} {}".format(i, j, k))


