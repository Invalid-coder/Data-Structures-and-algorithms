class PQElement:
    def __init__(self, key, priority):
        self.mKey = key
        self.mPriority = priority

    def updatePriority(self, priority):
        self.mPriority = priority

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

    def isEmpty(self):
        return len(self.items) == 1

    def insert(self, key, priority):
        el = PQElement(key, priority)
        self.size += 1
        self.items.append(el)
        self.elementsMap[key] = self.size
        self.siftUp()

    def extractMinimum(self):
        root = self.items[1].key()
        self.swap(-1, 1)
        self.items.pop()
        del self.elementsMap[root]
        self.size -= 1
        self.siftDown()

        return root

    def siftDown(self):
        i = 1

        while (2 * i) <= self.size:
            left = 2 * i
            right = 2 * i + 1
            minChild = self.minChild(left, right)

            if self.items[minChild] < self.items[i]:
                self.swap(i, minChild)
                i = minChild
            else:
                break

    def siftUp(self):
        i = len(self.items) - 1

        while i > 1:
            parent = i // 2

            if self.items[i] < self.items[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def swap(self, i, j):
        key_i = self.items[i].key()
        key_j = self.items[j].key()
        self.elementsMap[key_i] = j
        self.elementsMap[key_j] = i
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def __contains__(self, item):
        return item in self.elementsMap

    def minChild(self, left, right):
        if right > self.size:
            return left
        else:
            if self.items[left] < self.items[right]:
                return left
            else:
                return right

    def updatePriority(self, key, priority):
        i = self.elementsMap[key]
        self.items[i].updatePriority(priority)

        while i > 1:
            parent = i // 2

            if self.items[i] < self.items[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

        return True