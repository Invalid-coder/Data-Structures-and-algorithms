#https://www.e-olymp.com/uk/submissions/7293994

def insertionSort(array):
    n = len(array)

    for i in range(1, n):
        currentValue = array[i]
        pos = i

        while pos > 0:
            if array[pos - 1] > currentValue:
                array[pos] = array[pos - 1]
            else:
                break

            pos -= 1

        array[pos] = currentValue

        if pos != i:
            print(' '.join(map(str, array)))

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    insertionSort(array)