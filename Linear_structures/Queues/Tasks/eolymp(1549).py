#https://www.e-olymp.com/uk/submissions/7484502

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
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
        node = self.front
        s = ""

        while not node is None:
            s += ' ' + node.item
            node = node.next

        return s

    def __len__(self):
        return self.size

if __name__ == '__main__':
    queue = Queue()

    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            text = input.readlines()
            i = 0

            while i < len(text) - 1:
                n, m, k = map(int, text[i].rstrip().split())
                victims = []

                for j in range(n):
                    queue.append('Gared')

                for j in range(m):
                    queue.append('Keka')

                while True:
                    if len(victims) == 2:
                        if victims[0] == victims[1]:
                            queue.append('Gared')
                        else:
                            queue.append('Keka')

                        victims.clear()

                    if len(queue) == 1 and not victims:
                        break

                    for j in range(k - 1):
                        queue.append(queue.pop())

                    victims.append(queue.pop())

                print(queue.pop(), file=output)
                i += 1