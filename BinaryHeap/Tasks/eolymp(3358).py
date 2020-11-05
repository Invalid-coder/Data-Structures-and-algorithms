#https://www.e-olymp.com/uk/submissions/7647170

class PQElement:
    def __init__(self, key, priority):
        self.mKey = key
        self.mPriority = priority

    def key(self):
        return self.mKey

    def priority(self):
        return self.mPriority

    def updatePriority(self, priority):
        self.mPriority = priority

    def __gt__(self, other):
        return self.mPriority > other.mPriority or self.mPriority == other.mPriority and self.mKey < other.mKey

class PriorityQueue:
    def __init__(self):
        self.items = [PQElement(0, 0)]
        self.elementsMap = {}
        self.size = 0

    def empty(self):
        return self.size == 0

    def top(self):
        return self.items[1].key() if not self.empty() else 0

    def insert(self, key):
        if not key in self.elementsMap:
            el = PQElement(key, 1)
            self.items.append(el)
            self.size += 1
            self.elementsMap[key] = self.size
            self.siftUp()
        else:
            self.updatePriority(key, 1)

    def swap(self, i, j):
        key_i = self.items[i].key()
        key_j = self.items[j].key()
        self.elementsMap[key_i] = j
        self.elementsMap[key_j] = i
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def maxChild(self, left, right):
        if right > self.size:
            return left
        else:
            if self.items[left] > self.items[right]:
                return left
            else:
                return right

    def siftDown(self, pos=None):
        if pos is None:
            i = 1
        else:
            i = pos

        while (2 * i) <= self.size:
            left = 2 * i
            right = left + 1
            maxChild = self.maxChild(left, right)

            if self.items[maxChild] > self.items[i]:
                self.swap(maxChild, i)
                i = maxChild
            else:
                break

    def siftUp(self, pos=None):
        if pos is None:
            i = self.size
        else:
            i = pos

        while i > 1:
            parent = i // 2

            if self.items[i] > self.items[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def updatePriority(self, key, a):
        i = self.elementsMap[key]
        prev = self.items[i].priority()
        self.items[i].updatePriority(prev + a)

        if self.items[i].priority() == 0:
            self.swap(i, -1)
            self.items.pop()
            del self.elementsMap[key]
            self.size -= 1
            self.siftDown(i)
        elif prev + a > prev:
            self.siftUp(i)
        else:
            self.siftDown(i)

    def execute(self, command, x):
        if command == '+':
            self.insert(x)
        else:
            self.updatePriority(x, -1)

        return self.top()

if __name__ == '__main__':
    n = int(input())
    pq = PriorityQueue()

    for i in range(n):
        command, x = input().split()
        x = int(x)

        res = pq.execute(command, x)

        print(res)
