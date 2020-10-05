#https://www.e-olymp.com/uk/submissions/7293961

def greater(a, b):
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if ord(a[i]) > ord(b[j]):
            return a
        elif ord(a[i]) < ord(b[j]):
            return b
        else:
            i += 1
            j += 1

    if i == len(a) and j < len(b):
        return b
    elif j == len(b) and i < len(a):
        return a
    else:
        return a

def selectionSort(array):
    n = len(array)

    for i in range(n - 1, 0, -1):
        maxpos = 0

        for j in range(1, i + 1):
            if greater(array[maxpos], array[j]) == array[j]:
                maxpos = j

        array[i], array[maxpos] = array[maxpos], array[i]

if __name__ == '__main__':
    n = int(input())
    array = [input() for _ in range(n)]

    selectionSort(array)

    for el in array:
        print(el)