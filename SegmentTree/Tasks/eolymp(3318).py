#https://www.e-olymp.com/uk/submissions/7669073

class SegmentTree:
    def __init__(self, array):
        n = len(array)
        self.items = 2 * n * [0]

        for i in range(n):
            self.items[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[2 * i] + self.items[2 * i + 1]

        self.size = n

    def update(self, left, right):
        left += self.size
        right += self.size

        for i in range(left, right + 1):
            self.items[i] = (self.items[i] * self.items[i]) % 2010

        while left != 1:
            left //= 2
            right //= 2

            for i in range(left, right + 1):
                self.items[i] = self.items[2 * i] + self.items[2 * i + 1]

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

    for _ in range(m):
        k, l, r = map(int, input().split())

        if k == 1:
            tree.update(l - 1, r - 1)
        else:
            print(tree. sum(l - 1, r - 1))