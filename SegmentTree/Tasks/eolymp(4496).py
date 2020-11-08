class SegmentTree:
    def __init__(self, array):
        n = len(array)
        self.items = 2 * n * [0]

        for i in range(n):
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
        left += self.size
        right += self.size
        res = 0

        while left <= right:
            if left % 2 == 1:
                res += self.items[left]
                left += 1
            if right % 2 == 0:
                res += self.items[right]
                right -= 1

            left //= 2
            right //= 2

        return res

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())
    tree = SegmentTree(array)

    for i in range(m):
        data = tuple(map(int, input().split()))

        if data[0] == 1:
            v = data[1]
            counter = 0

            for i in range(n):
                if tree.sum(0, i) <= v:
                    counter += 1
                else:
                    break

            print(counter)
        else:
            tree.update(data[1] - 1, data[2])