class PQElement:
    def __init__(self, key, priority):
        self.mKey = key
        self.mPriority = priority

    def updatePriority(self, priority):
        self.mPriority = priority

    def key(self):
        return self.mKey

    def priority(self):
        return self.mPriority

    def key(self):
        return self.mKey

    def __lt__(self, other):
        return self.mPriority < other.mPriority

    def __le__(self, other):
        return self.mPriority <= other.mPriority

    def __gt__(self, other):
        return self.mPriority > other.mPriority

    def __ge__(self, other):
        return self.mPriority >= other.mPriority

class PriorityQueue:
    def __init__(self):
        self.items = [PQElement(0, 0)]
        self.size = 0
        self.elementsMap = {}

    def swap(self, i, j):
        key_i = self.items[i].key()
        key_j = self.items[j].key()
        self.elementsMap[key_i] = j
        self.elementsMap[key_j] = i
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def add(self, key, priority):
        el = PQElement(key, priority)
        self.size += 1
        self.items.append(el)
        self.elementsMap[key] = self.size
        self.siftUp()

    def pop(self):
        self.swap(1, -1)
        item = self.items.pop()
        del self.elementsMap[item.key()]
        self.size -= 1
        self.siftDown()

        return (item.key(), item.priority())

    def change(self, key, priority):
        i = self.elementsMap[key]
        self.items[i].updatePriority(priority)

        while i > 1:
            parent = i // 2

            if self.items[i] > self.items[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def siftUp(self):
        i = len(self.items) - 1

        while i > 1:
            parent = i // 2

            if self.items[i] > self.items[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def siftDown(self):
        i = 1

        while (2 * i) <= self.size:
            left = 2 * i
            right = left + 1
            maxChild = self.maxChild(left, right)

            if self.items[maxChild] > self.items[i]:
                self.swap(i, maxChild)
                i = maxChild
            else:
                break

    def maxChild(self, left, right):
        if right > self.size:
            return left
        else:
            if self.items[left] > self.items[right]:
                return left
            else:
                return right

    def execute(self, command):
        command = command.split()
        name = command[0].lower()

        if name == "pop":
            return self.pop()
        else:
            args = command[1:]

            getattr(self, name)(*args)


if __name__ == '__main__':
    pq = PriorityQueue()

    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            for line in input:
                res = pq.execute(line.rstrip())

                if res:
                    print(*res, file=output)

