#https://www.e-olymp.com/uk/submissions/7390294

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

        self.top = node

    def pop(self):
        current_top = self.top
        item = current_top.item
        self.top = current_top.next
        del current_top
        return item

def get_char_digit(digit):
    if digit <= 9:
        return str(digit)
    else:
        return '[{}]'.format(digit)

def convert(num, base):
    stack = Stack()

    while num > 0:
        stack.push(num % base)
        num //= base

    converted = ''

    while not stack.empty():
        converted += get_char_digit(stack.pop())

    return converted

if __name__ == '__main__':
    A = int(input())
    P = int(input())
    print(convert(A, P))
