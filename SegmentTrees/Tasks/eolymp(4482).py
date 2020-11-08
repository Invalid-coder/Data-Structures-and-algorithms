#https://www.e-olymp.com/uk/submissions/7666387

class SegmentTree:
    def __init__(self, array, name):
        n = len(array)
        self.items = 2 * n * [0]

        for i in range(n):
            self.items[n + i] = array[i]

        for i in range(n - 1, 0, -1):
            self.items[i] = getattr(self, name)(self.items[2 * i], self.items[2 * i + 1])

        self.size = n
        self.name = name

    def gcd(self, a, b):
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a

        return a + b

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def update(self, pos, val):
        pos += self.size
        self.items[pos] = val
        i = pos // 2

        while i > 0:
            self.items[i] = getattr(self, self.name)(self.items[2 * i], self.items[2 * i + 1])
            i //= 2

    def intervalValue(self, left, right):
        left += self.size
        right += self.size
        res = None

        while left <= right:
            if left % 2 == 1:
                res = getattr(self, self.name)(res, self.items[left]) if res else self.items[left]
                left += 1
            if right % 2 == 0:
                res = getattr(self, self.name)(res, self.items[right]) if res else self.items[right]
                right -= 1

            left //= 2
            right //= 2

        return res

def wins(a, b):
    if a < b:
        return "wins"
    elif a > b:
        return "loser"
    else:
        return "draw"

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())
    tree1 = SegmentTree(array, "gcd")
    tree2 = SegmentTree(array, "lcm")

    for _ in range(m):
        q, l, r = map(int, input().split())

        if q == 1:
            a = tree1.intervalValue(l - 1, r - 1)
            b = tree2.intervalValue(l - 1, r - 1)
            print(wins(a, b))
        else:
            tree1.update(l - 1, r)
            tree2.update(l - 1, r)
