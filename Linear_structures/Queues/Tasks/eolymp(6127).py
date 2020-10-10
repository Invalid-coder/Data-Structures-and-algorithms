#https://www.e-olymp.com/uk/submissions/7482856

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue():
    def __init__(self):
        self.front_node = None
        self.back_node = None
        self.currentSize = 0

    def empty(self):
        return self.front_node is None and self.back_node is None

    def push(self, item):
        node = Node(item)

        if self.empty():
            self.front_node = node
        else:
            self.back_node.next = node

        self.back_node = node
        self.currentSize += 1

        return "ok"

    def pop(self):
        if self.empty():
            return "error"

        front = self.front_node
        item = front.item
        self.front_node = self.front_node.next
        del front

        if self.front_node is None:
            self.back_node = None

        self.currentSize -= 1
        return item

    def clear(self):
        while not self.front_node is None:
            front = self.front_node
            self.front_node = front.next
            del front

        self.back_node = None
        self.currentSize = 0

        return "ok"

    def front(self):
        if self.empty():
            return "error"

        return self.front_node.item

    def size(self): return self.currentSize
    def exit(self): return "bye"

    def execute(self, command):
        if command.startswith("push"):
            return self.push(command[5:])
        else:
            return getattr(self, command)()


if __name__ == '__main__':
    queue = Queue()

    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            for line in input:
                res = queue.execute(line.rstrip())

                print(res, file=output)

                if res == "bye":
                    break