#https://www.e-olymp.com/uk/submissions/7483298

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque():
    def __init__(self):
        self.front_node = None
        self.back_node = None
        self.currentSize = 0

    def empty(self):
        return self.front_node is None and self.back_node is None

    def push_back(self, item):
        node = Node(item)
        node.prev = self.back_node

        if self.empty():
            self.front_node = node
        else:
            self.back_node.next = node

        self.back_node = node
        self.currentSize += 1
        return "ok"

    def pop_back(self):
        if self.empty():
            return "error"

        back = self.back_node
        item = back.item
        self.back_node = self.back_node.prev
        self.currentSize -= 1
        del back

        if self.back_node is None:
            self.front_node = None
        else:
            self.back_node.next = None

        return item

    def push_front(self, item):
        node  = Node(item)
        node.next = self.front_node

        if self.empty():
            self.back_node = node
        else:
            self.front_node.prev = node

        self.front_node = node
        self.currentSize += 1
        return "ok"

    def pop_front(self):
        if self.empty():
            return "error"

        front = self.front_node
        item = front.item
        self.front_node = self.front_node.next
        self.currentSize -= 1
        del front

        if self.front_node is None:
            self.back_node = None
        else:
            self.front_node.prev = None

        return item

    def front(self):
        if self.empty():
            return "error"

        return self.front_node.item

    def back(self):
        if self.empty():
            return "error"

        return self.back_node.item

    def clear(self):
        while not self.front_node is None:
            front = self.front_node
            self.front_node = self.front_node.next
            del front

        self.back_node = None
        self.currentSize = 0
        return "ok"

    def size(self): return self.currentSize
    def exit(self): return "bye"

    def execute(self, command):
        command = command.split()
        name = command[0]
        args = command[1:]

        return getattr(self, name)(*args)

if __name__ == '__main__':
    deque = Deque()

    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            for line in input:
                res = deque.execute(line.rstrip())
                print(res, file=output)

                if res == "bye":
                    break





