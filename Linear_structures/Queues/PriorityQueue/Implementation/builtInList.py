class PriorotyQueue:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def insert(self, prioroty, item):
        self.items.append((prioroty, item))

    def extract_minimum(self):
        if self.empty():
            raise Exception("PQueue: 'extract_minimum applied to an empty container")

        minpos = 0

        for i in range(1, len(self.items)):
            if self.items[minpos][0] > self.items[i][0]:
                minpos = i

        return self.items.pop(minpos)[1]