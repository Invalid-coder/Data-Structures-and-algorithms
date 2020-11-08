#https://www.e-olymp.com/uk/submissions/7649284

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

    def plus(self, i, item):
        ''' Додає до елемента на позиції i (початок з нуля) елемент item.'''
        i += self.size
        self.items[i] += item
        while i != 1:  # Поки не дійшли до кореня
            i = i // 2 # Беремо номер батька
            # Визначаємо його навантаження
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]

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
            if command[0] == '+':
                tree.plus(int(command[1]) - 1, int(command[2]))
            elif command[0] == '?':
                print(tree.sum(int(command[1]) - 1, int(command[2]) - 1))
