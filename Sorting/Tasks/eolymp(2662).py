#https://www.e-olymp.com/uk/submissions/7302737

def selection_sort(array):
    n = len(array)
    first = array[0]
    counter = 0

    for i in range(n - 1):
        minpos = n - 1

        for j in range(n - 2, i - 1, -1):
            if array[minpos] > array[j]:
                minpos = j

        if array[minpos] == first or array[i] == first:
            if array[minpos] != array[i]:
                counter += 1

        array[i], array[minpos] = array[minpos], array[i]


    return counter

if __name__ == '__main__':
    N = int(input())
    array = list(map(int, input().split()))

    print(selection_sort(array))