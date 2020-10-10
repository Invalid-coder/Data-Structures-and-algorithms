class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.empty():
            raise Exception("Queue: 'dequeue' applied to an empty container")

        return self.items.pop(0)

    def __len__(self):
        return len(self.items)
