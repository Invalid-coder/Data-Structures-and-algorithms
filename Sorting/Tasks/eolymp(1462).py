def lastDigit(num):
    return num % 10

def greater(a, b):
    if lastDigit(a) > lastDigit(b):
        return a
    elif lastDigit(a) < lastDigit(b):
        return b
    else:
        if a > b:
            return a
        else:
            return b

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        currentValue = array[i]
        pos = i

        while pos > 0:
            if greater(array[pos - 1], currentValue) == array[pos - 1]:
                array[pos] = array[pos - 1]
            else:
                break

            pos -= 1

        array[pos] = currentValue

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
    N = input()
    array = list(map(int, input().split()))
    bubble_sort(array)

    print(*array)