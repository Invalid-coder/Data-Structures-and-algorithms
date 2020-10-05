def w(num):
    s = 0

    while num > 0:
        s += num % 10
        num //= 10

    return s

def lexicographically_greater(a, b):
    a = str(a)
    b = str(b)
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if int(a[i]) > int(b[j]):
            return int(a)
        elif int(a[i]) < int(b[j]):
            return int(b)

        i += 1
        j += 1

    if i == len(a) and j != len(b):
        return int(b)
    else:
        return int(a)

def greater(a, b):
    w1 = w(a)
    w2 = w(b)

    if w1 < w2:
        return b
    elif w1 > w2:
        return a
    else:
        return lexicographically_greater(a, b)

def selection_sort(array):
    n = len(array)

    for i in range(n - 1, 0, -1):
        max_pos = 0

        for j in range(1, i + 1):
            if w(array[j]) > w(array[max_pos]):
                max_pos = j
            elif w(array[j]) == w(array[max_pos]):
                if lexicographically_greater(array[j], array[max_pos]) == array[j]:
                    max_pos = j

        array[i], array[max_pos] = array[max_pos],array[i]

def bubble_sort(array):
    n = len(array)

    for pass_num in range(n - 1, 0, -1):
        isSorted = True

        for i in range(pass_num):
            if greater(array[i], array[i + 1]) == array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False

        if isSorted:
            break

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    array = [i for i in range(1, n + 1)]
    bubble_sort(array)#selection_sort(array)

    print(array.index(k) + 1)
    print(array[k - 1])

