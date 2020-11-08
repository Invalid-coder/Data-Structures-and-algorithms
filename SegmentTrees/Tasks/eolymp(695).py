#https://www.e-olymp.com/uk/submissions/7667349

MAX_VAL = 1e9
MIN_VAL = -1e9
n = 100000
a = [(i * i) % 12345 + (i * i * i) % 23456 for i in range(1, n + 1)]

class SegmentTree:
    def __init__(self, val, name):
        self.items = 2 * n * [val]

        for i in range(n):
            self.items[n + i] = a[i]

        for i in range(n - 1, 0, -1):
            self.items[i] = getattr(self, name)(self.items[2 * i], self.items[2 * i + 1])

        self.size = n
        self.name = name

    def update(self, pos, value):
        pos += self.size
        self.items[pos] = value
        i = pos // 2

        while i > 0:
            self.items[i] = getattr(self, self.name)(self.items[2 * i], self.items[2 * i + 1])
            i //= 2

    def max(self, a, b):
        return max(a, b)

    def min(self, a, b):
        return min(a, b)

    def max_on_interval(self, left, right):
        left += self.size
        right += self.size
        res = MIN_VAL

        while left <= right:
            if left % 2 == 1:
                res = max(res, self.items[left])
                left += 1
            if right % 2 == 0:
                res = max(res, self.items[right])
                right -= 1

            left //= 2
            right //= 2

        return res

    def min_on_interval(self, left, right):
        left += self.size
        right += self.size
        res = MAX_VAL

        while left <= right:
            if left % 2 == 1:
                res = min(res, self.items[left])
                left += 1
            if right % 2 == 0:
                res = min(res, self.items[right])
                right -= 1

            left //= 2
            right //= 2

        return res

if __name__ == '__main__':
    k = int(input())
    tree_max = SegmentTree(MIN_VAL, "max")
    tree_min = SegmentTree(MAX_VAL, "min")

    for i in range(k):
        x, y = map(int, input().split())

        if x > 0:
            max_el = tree_max.max_on_interval(x - 1, y - 1)
            min_el = tree_min.min_on_interval(x - 1, y - 1)
            print(max_el - min_el)
        else:
            tree_max.update(-x - 1, y)
            tree_min.update(-x - 1, y)

