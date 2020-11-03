#https://www.e-olymp.com/uk/submissions/7628403

class BinaryHeap:
    def __init__(self):
        self.items = [0]
        self.size = 0

    def isEmpty(self):
        return len(self.items) == 1

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.siftUp()

    def extractMinimum(self):
        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
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
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def minChild(self, left, right):
        if right > self.size:
            return left
        else:
            if self.items[left] < self.items[right]:
                return left
            else:
                return right

    def __len__(self):
        return self.size

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    heap = BinaryHeap()

    for x in arr:
        heap.insert(x)

    minCost = 0

    while len(heap) > 1:
        c1 = heap.extractMinimum()
        c2 = heap.extractMinimum()
        cost = c1 + c2
        minCost += cost
        heap.insert(cost)

    print(minCost)
