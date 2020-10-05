#https://www.e-olymp.com/uk/submissions/7307240

swaps = 0

def bubble_sort(array):
    global swaps

    n = len(array)

    for pass_num in range(n - 1, 0, -1):
        isSorted = True

        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
                swaps += 1

        if isSorted:
            break

if __name__ == '__main__':
    tests = []

    with open("input.txt") as inp:
        text = inp.readlines()
        i = 0

        while i < len(text) - 1:
            n = int(text[i])
            tests.append(list(map(lambda x: int(x.rstrip()), text[i + 1: i + n + 1])))
            i += (n + 1)

    for arr in tests:
        bubble_sort(arr)
        print(swaps)
        swaps = 0
