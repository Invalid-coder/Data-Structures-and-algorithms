#https://www.e-olymp.com/uk/submissions/7649572

from math import log2, ceil

class SegmentTree:
    ''' Дерево відрізків з операцією суми.'''

    def __init__(self, array):
        k = len(array)
        n = 1 << ceil(log2(k))
        self.items = n * [0] + array + (n - k) * [0]
        for i in range(n - 1, 0, -1):
            # Визначаємо навантаження предків
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]
        self.size = n

    def update(self, left, right, item):
        ''' Міняє елемент масиву на позиціях i - j (початок з нуля) на item.'''
        left += self.size
        right += self.size

        for k in range(left, right + 1):
            self.items[k] = item

        while left != 1:
            left = left // 2
            right = right // 2

            self.items[left] = self.items[2 * left] + self.items[2 * left + 1]
            self.items[right] = self.items[2 * right] + self.items[2 * right + 1]

            item = self.items[2 * left + 2] + self.items[2 * left + 3]

            for i in range(left + 1, right):
                self.items[i] = item

    def sum(self, left, right):
        ''' Повертає суму елементів відрізка.'''
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left % 2 == 1: # Якщо правий син
                result += self.items[left]
            if right % 2 == 0: # Якщо лівий син
                result += self.items[right]
            left = (left + 1) // 2   # Беремо індекс батька вузла справа
            right = (right - 1) // 2 # Беремо індекс батька вузла зліва
        return result

if __name__ == '__main__':
    with open('input.txt') as inp:
        n, q = map(int, inp.readline().split())
        array = list(map(int, inp.readline().split()))
        tree = SegmentTree(array)
        for _ in range(q):
            command = inp.readline().split()
            if command[0] == '=':
                tree.update(int(command[1]) - 1, int(command[2]) - 1, int(command[3]))
            elif command[0] == '?':
                print(tree.sum(int(command[1]) - 1, int(command[2]) - 1))