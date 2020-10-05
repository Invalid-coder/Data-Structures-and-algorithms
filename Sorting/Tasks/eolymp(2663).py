#https://www.e-olymp.com/uk/submissions/7293934

def swappingCounter(array):
    counter = 0
    n = len(array)

    for pass_num in range(n - 1, 0, -1):
        isSorted = True

        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
                counter += 1

        if isSorted:
            break

    return counter

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    print(swappingCounter(array))