"""
Пошук всіх перестановок заданої послідовності.
"""

def sequences(lst, k, n):
    """
    :param lst: підсписок перестановок
    :param k:   елемент для вставки
    :param n:   найбільший елемент послідовності
    """

    if k > n:
        print(*lst)
        return

    for pos in range(k):
        new_lst = lst[:]
        new_lst.insert(pos, k)
        sequences(new_lst, k + 1, n)

if __name__ == '__main__':
    n = int(input())
    lst = []
    sequences(lst, 1, n)
