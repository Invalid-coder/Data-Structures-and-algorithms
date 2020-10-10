#https://www.e-olymp.com/uk/submissions/7485531

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.min = None

class Stack():
    def __init__(self):
        self.back = None

    def empty(self):
        return self.back is None

    def push(self, item):
        node = Node(item)

        if self.empty():
            node.min = item
        else:
            node.next = self.back
            node.min = min(item, self.back.min)

        self.back = node

    def pop(self):
        if not self.empty():
            back = self.back
            item = back.item
            self.back = self.back.next
            del back
            return item

    def top(self):
        return self.back

if __name__ == '__main__':
    n, a, b, c, x = map(int, input().split())
    head = Stack()
    tail = Stack()
    result = 0

    for i in range(n):
        x = ((a * x * x + (b * x) + c) // 100) % 1000000

        if x % 5 < 2:
            if head.empty():
                while not tail.empty():
                    value = tail.pop()
                    head.push(value)

            if not head.empty():
                head.pop()
        else:
            tail.push(x)

        if not tail.empty() and not head.empty():
            result += min(tail.top().min, head.top().min)
        else:
            if not tail.empty():
                result += tail.top().min
            elif not head.empty():
                result += head.top().min

    print(result)

