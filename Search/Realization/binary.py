def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] < x:
            left = mid + 1
        elif array[mid] > x:
            right = mid - 1
        else:
            return mid

    return None

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

def binary_continuous(f, c, a, b):
    left = a
    right = b
    mid = (left + right) / 2.0

    while left != mid and right != mid:
        if f(mid) < c:
            left = mid
        else:
            right = mid

        mid = (left + right) / 2.0