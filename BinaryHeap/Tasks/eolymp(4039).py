#https://www.e-olymp.com/uk/submissions/7620189

class BinaryHeap:
    names = {'0': "insert", '1': "extractMax"}

    def __init__(self):
        self.items = [0]
        self.size = 0

    def isEmpty(self):
        return len(self.items) == 1

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.siftUp()

    def extractMax(self):
        if self.isEmpty():
            raise Exception("Extract applied to an empty container")

        self.swap(1, -1)
        item = self.items.pop()
        self.size -= 1
        self.siftDown()

        return item

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

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

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

        if command[0] == '0':
            self.insert(int(command[1]))
        else:
            return self.extractMax()

if __name__ == '__main__':
    n = int(input())
    heap = BinaryHeap()

    for i in range(n):
        command = input()
        res = heap.execute(command)

        if res:
            print(res)