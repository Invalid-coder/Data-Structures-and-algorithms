#https://www.e-olymp.com/uk/submissions/7324646

def sequences(lst, n):
    """

    :param lst: підсписок перестановок
    :param n: найбільшій елемент послідовності
    :return:
    """

    k = len(lst)

    if k == n:
        print(*lst)
        return

    for i in range(1, n + 1):
        if i not in lst:
            new_lst = lst[:]
            new_lst.append(i)
            sequences(new_lst, n)

if __name__ == '__main__':
    n = int(input())
    lst = []
    sequences(lst, n)