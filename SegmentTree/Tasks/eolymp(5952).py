class SegmentTree:
    def __init__(self):
        self.size = 256
        self.items = 2 * self.size * [0]

    def add(self, i, j, value):
        i += self.size
        j += self.size

        for k in range(i, j + 1):
            self.items[k] += value

        while i != 1:
            i //= 2
            j //= 2

            for k in range(i, j + 1):
                self.items[k] = self.items[2 * k] + self.items[2 * k + 1]

    def get(self, left, right):
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
    q, L, R, p = map(int, input().split())
    tree = SegmentTree()
    tree.add(L, R, 1)

    for i in range(q - 1):
        L_new = tree.get(min(L, R), max(L, R)) % p
        R_new = 255 - L_new
        tree.add(min(L_new, R_new), max(L_new, R_new), 1)
        L, R = L_new, R_new

    print(tree.get(0, 255))