class Stack:
    """
        Implementation by built-in list
    """

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def top(self):
        if self.empty():
            raise Exception("Stack: 'top' applied to an empty container")
        else:
            return self.items[-1]

    def pop(self):
        if self.empty():
            raise Exception("Stack 'pop' applied to an empty container")
        else:
            return self.items.pop()

    def __len__(self):
        return len(self.items)

if __name__ == '__main__':
    stack = Stack()
    stack.push(35)
    stack.push(37)
    stack.push(77)
    print(stack.top())
    print(stack.pop())
    print(stack.top())

