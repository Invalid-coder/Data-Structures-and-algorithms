#https://www.e-olymp.com/uk/submissions/7298168

def seconds(data):
    return (data[0] * 3600) + (data[1] * 60) + data[2]

def greater(a, b):
    s1 = seconds(a)
    s2 = seconds(b)

    if s1 == 0:
        return a
    elif s2 == 0:
        return b
    else:
        return a if s1 > s2 else b

def selectionSort(array):
    n = len(array)

    for i in range(n - 1, 0, -1):
        maxpos = 0

        for j in range(1, i + 1):
            if greater(array[maxpos], array[j]) == array[j]:
                maxpos = j

        array[i], array[maxpos] = array[maxpos], array[i]

if __name__ == '__main__':
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    selectionSort(array)

    for data in array:
        print(' '.join(list(map(str, data))))
