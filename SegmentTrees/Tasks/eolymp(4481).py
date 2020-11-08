#https://www.e-olymp.com/uk/submissions/7650011

from math import ceil, log2

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        n = 1 << ceil(log2(k))
        self.items = n * [0] + array + (n - k) * [0]

        for i in range(n - 1, 0, -1):
            self.items[i] = self.gcd(self.items[2 * i], self.items[2 * i + 1])

        self.size = n

    def gcd(self, a, b):
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a

        return a + b

    def update(self, i, val):
        i += self.size
        self.items[i] = val

        while i > 0:
            i //= 2
            self.items[i] = self.gcd(self.items[2 * i], self.items[2 * i + 1])

    def func(self, left, right):
        left += self.size
        right += self.size
        res = None

        while left <= right:
            if left % 2 == 1:
                res = self.gcd(res, self.items[left]) if not res is None else self.items[left]
            if right % 2 == 0:
                res = self.gcd(res, self.items[right]) if not res is None else self.items[right]

            left = (left + 1) // 2
            right = (right - 1) // 2

        return res

if __name__ == '__main__':
    with open('input.txt') as inp:
        n = int(inp.readline())
        array = list(map(int, inp.readline().split()))
        m = int(inp.readline())
        tree = SegmentTree(array)

        for _ in range(m):
            q,l,r = map(int, inp.readline().split())

            if q == 1:
                print(tree.func(l - 1, r - 1))
            else:
                tree.update(l - 1, r)