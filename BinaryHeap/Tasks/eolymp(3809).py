#https://www.e-olymp.com/uk/submissions/7630134

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

    def extractMaximum(self):
        self.swap(-1, 1)
        item = self.items.pop()
        del self.elementsMap[item.key()]
        self.size -= 1
        self.siftDown()

        return item.key(), item.priority()

    def siftDown(self):
        i = 1

        while (2 * i) <= self.size:
            left = 2 * i
            right = 2 * i + 1
            maxChild = self.maxChild(left, right)

            if self.items[maxChild] > self.items[i]:
                self.swap(i, maxChild)
                i = maxChild
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

    def swap(self, i, j):
        key_i = self.items[i].key()
        key_j = self.items[j].key()
        self.elementsMap[key_i] = j
        self.elementsMap[key_j] = i
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def __contains__(self, item):
        return item in self.elementsMap

    def maxChild(self, left, right):
        if right > self.size:
            return left
        else:
            if self.items[left] > self.items[right]:
                return left
            else:
                return right

    def updatePriority(self, key, priority):
        i = self.elementsMap[key]
        self.items[i].updatePriority(priority)

        while i > 1:
            parent = i // 2

            if self.items[i] > self.items[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

        return True

    def clear(self):
        self.items = [PQElement(0, 0)]

def getNegativeEnergy(pq, arr, n):
    time = 1
    negativeEnergy = 0
    i = 0

    while i < 100001:
        while arr[i][0] == time:
            pq.insert(arr[i][0], arr[i][1])
            i += 1

            if i == n:
                break

        if i == n:
            break

        if pq.isEmpty():
            if i < n:
                time = max(time + 1, arr[i][0])
            else:
                time += 1
        else:
            r, w = pq.extractMaximum()
            negativeEnergy += (time - r) * w
            time += 1

    while not pq.isEmpty():
        r, w = pq.extractMaximum()
        negativeEnergy += (time - r) * w
        time += 1

    return negativeEnergy

if __name__ == '__main__':
    t = int(input())
    pq = PriorityQueue()

    for i in range(t):
        n = int(input())
        arr = []

        for j in range(n):
            item = tuple(map(int, input().split()))
            arr.append(item)

        arr = sorted(arr, key=lambda x:x[0])
        print(getNegativeEnergy(pq, arr, n))