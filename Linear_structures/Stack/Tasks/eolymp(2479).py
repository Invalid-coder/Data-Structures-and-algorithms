#https://www.e-olymp.com/uk/submissions/7390155

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

    def back(self):
        return self.top.item

    def pop(self):
        current_top = self.top
        self.top = current_top.next
        del current_top

def isCorrect(brackets):
    stack = Stack()
    b = {')': '(', ']': '['}

    for bracket in brackets:
        if bracket in '([':
            stack.push(bracket)
        else:
            if stack.empty():
                return False

            if stack.back() != b[bracket]:
                return False
            else:
                stack.pop()

    return stack.empty()

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print('Yes' if isCorrect(input()) else 'No')