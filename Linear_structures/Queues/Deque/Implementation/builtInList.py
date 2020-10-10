class Deque:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def append(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            raise Exception("Deque: 'pop' applied to an empty container")

        return self.items.pop()

    def appendLeft(self, item):
        self.items.insert(0, item)

    def popLeft(self):
        if self.empty():
            raise Exception("Deque: 'popLeft' applied to an empty container")

        return self.items.pop(0)