#https://www.e-olymp.com/uk/submissions/7306769

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
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1

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
    n = int(input())
    array = list(map(int, input().split()))
    merge_sort(array)

    print(*array)