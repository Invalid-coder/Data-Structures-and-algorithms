#https://www.e-olymp.com/uk/submissions/7670443

class SegmentTree:
    def __init__(self, array):
        n = len(array)
        self.items = 2 * n * [0]

        for i in range(n):
            self.items[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[2 * i] * self.items[2 * i + 1]

        self.size = n

    def update(self, pos, val):
        pos += self.size
        self.items[pos] = val
        i = pos // 2

        while i > 0:
            self.items[i] = self.items[2 * i] * self.items[2 * i + 1]
            i //= 2

    def product(self, left, right):
        left += self.size
        right += self.size
        res = 1

        while left <= right:
            if left % 2 == 1:
                res *= self.items[left]
                left += 1
            if right % 2 == 0:
                res *= self.items[right]
                right -= 1

            if res == 0:
                return '0'

            left //= 2
            right //= 2

        return '+' if res > 0 else '-'

if __name__ == '__main__':
    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            lines = input.readlines()
            i = 0

            while i < len(lines):
                n, m = map(int, lines[i].split())
                i += 1
                array = list(map(int, lines[i].split()))
                i += 1
                tree = SegmentTree(array)
                ans = ''

                for j in range(m):
                    q, l, r = lines[i].split()
                    i += 1

                    if q == 'C':
                        tree.update(int(l) - 1, int(r))
                    else:
                        ans += tree.product(int(l) - 1, int(r) - 1)

                print(ans)