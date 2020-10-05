#https://www.e-olymp.com/uk/submissions/7375203

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack():
    def __init__(self):
        self.top_node = None
        self.currentSize = 0

    def empty(self):
        return self.top_node is None

    def push(self, item):
        node = Node(item)

        if not self.empty():
            node.next = self.top_node

        self.top_node = node
        self.currentSize += 1

        return 'ok'

    def back(self):
        if self.empty():
            return 'error'
        else:
            return self.top_node.item

    def pop(self):
        if self.empty():
            return 'error'
        else:
            current_top = self.top_node
            item = current_top.item
            self.top_node = current_top.next
            self.currentSize -= 1
            del current_top
            return item

    def size(self):
        return self.currentSize

    def clear(self):
        self.currentSize = 0

        while not self.top_node is None:
            current_top = self.top_node
            self.top_node = current_top.next
            del current_top

        return 'ok'

    def exit(self):
        return 'bye'

    def execute(self, command):
        if command.startswith('push'):
            return self.push(command[5:])
        else:
            return getattr(self, command)()

if __name__ == '__main__':
    stack = Stack()

    with open('input.txt') as input:
        with open('output.txt', 'w') as output:
            for line in input:
                result = stack.execute(line.rstrip())
                print(result, file=output)

                if result == 'bye':
                    break