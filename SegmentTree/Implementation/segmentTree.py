from math import *

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        n = (1 << int(log2(k - 1)) + 1)
        self.items = 2 * n * [0]

        for i in range(k):
            self.items[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[2 * i] + self.items[2 * i + 1]

        self.size = n

    def update(self, pos, val):
        pos += self.size
        self.items[pos] = val

        i = pos // 2

        while i > 0:
            self.items[i] = self.items[2 * i] + self.items[2 * i + 1]
            i //= 2

    def sum(self, left, right):
        res = 0
        left += self.size
        right += self.size

        while left <= right:
            if left % 2 == 1:
                res += self.items[left]
            if right % 2 == 0:
                res += self.items[right]

            left = (left + 1) // 2
            right = (right - 1) // 2

        return res

if __name__ == '__main__':
    array = [2, 7, 6, 4, 1, 3, 5, 8]
    st = SegmentTree(array)
    print(st.sum(1, 6))