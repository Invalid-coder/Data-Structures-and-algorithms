#https://www.e-olymp.com/uk/submissions/7170096

def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] < x:
            left = mid + 1
        elif array[mid] > x:
            right = mid - 1
        else:
            return True

    return False

if __name__ == '__main__':
    n = input()
    array = list(map(int, input().split()))
    m = input()
    check = list(map(int, input().split()))

    for el in check:
        if binary_search(array, el):
            print('YES')
        else:
            print('NO')