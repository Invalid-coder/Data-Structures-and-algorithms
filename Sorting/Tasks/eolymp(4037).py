#https://www.e-olymp.com/uk/submissions/7306870

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][0] > righthalf[j][0]:
                array[k] = righthalf[j]
                j += 1
            else:
                array[k] = lefthalf[i]
                i += 1

            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1

if __name__ == '__main__':
    N = int(input())
    array = [tuple(map(int, input().split())) for _ in range(N)]
    merge_sort(array)

    for item in array:
        print(*item)