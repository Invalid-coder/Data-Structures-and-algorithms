#https://www.e-olymp.com/uk/submissions/7170105

def binary_leftmost(array, x):
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2

        if array[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left

def binary_rightmost(array, x):
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2

        if array[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left - 1

def count(array, el):
    return binary_rightmost(array, el) - binary_leftmost(array, el) + 1

if __name__ == '__main__':
    n = input()
    array = list(map(int, input().split()))
    m = input()
    check = list(map(int, input().split()))

    for el in check:
        print(count(array, el))