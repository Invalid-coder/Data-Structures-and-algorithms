class SegmentTree:
    def __init__(self, array):
        n = len(array)
        self.items = 2 * n * ['']

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
        res = ''

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
    n, k = map(int, input().split())
    array = input()
    tree = SegmentTree(array)
    ans = ''

    for _ in range(k):
        data = input().split()

        if data[0] == '*':
            tree.update(int(data[1]) - 1, data[2])
        else:
            left = int(data[1]) - 1
            right = int(data[2]) - 1
            length = int(data[3]) - 1
            a = tree.sum(left, left + length)
            b = tree.sum(right, right + length)
            ans += '+' if a == b else '-'

    print(ans)