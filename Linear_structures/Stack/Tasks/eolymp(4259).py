#https://www.e-olymp.com/uk/submissions/7376565

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def empty(self):
        return self.top is None

    def push(self, item):
        node = Node(item)

        if not self.empty():
            node.next = self.top

            if self.top.item < item:
                node.item = self.top.item

        self.top = node

    def pop(self):
        current_top = self.top
        self.top = current_top.next
        del current_top

    def getMin(self):
        return self.top.item

    def execute(self, command):
        if int(command[0]) == 1:
            self.push(int(command[2:]))
        elif int(command[0]) == 2:
            self.pop()
        else:
            return self.getMin()

        return None

if __name__ == '__main__':
    n = int(input())
    stack = Stack()

    for i in range(n):
        line = input()
        res = stack.execute(line)

        if res:
            print(res)
