#https://www.e-olymp.com/ru/submissions/7303125

def greater(a, b):
    k1, k2 = 0, 0

    for line in a:
        for c in line:
            if ord(' ') <= ord(c) <= ord('z'):
                k1 += 1

    for line in b:
        for c in line:
            if ord(' ') <= ord(c) <= ord('z'):
                k2 += 1

    if k1 > k2:
        return a
    elif k1 < k2:
        return b
    else:
        return None

def selection_sort(array):
    n = len(array)

    for i in range(n - 1, 0, -1):
        maxpos = 0

        for j in range(1, i + 1):
            greaterValue = greater(array[maxpos], array[j])

            if greaterValue == array[j]:
                maxpos = j

        array[i], array[maxpos] = array[maxpos], array[i]

if __name__ == '__main__':
    arr = []

    with open("eolymp(4230)/input.txt") as inp:
        n = int(inp.readline())

        for i in range(n):
            m = int(inp.readline())
            text = [inp.readline().rstrip() for _ in range(m)]
            arr.append(text)

    selection_sort(arr)

    for i, text in enumerate(arr):
        for line in text:
            print(line)

        if i < len(arr) - 1:
            print('***')





