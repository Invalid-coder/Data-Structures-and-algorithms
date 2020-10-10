def insertion_sort(array):
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