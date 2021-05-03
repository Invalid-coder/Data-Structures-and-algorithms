def selection_sort(array):
    n = len(array)

    for i in range(n - 1, 0, -1):
        maxpos = 0

        for j in range(1, i + 1):
            if array[maxpos] < array[j]:
                maxpos = j

        array[i], array[maxpos] = array[maxpos], array[i]
