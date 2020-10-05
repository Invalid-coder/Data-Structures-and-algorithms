#https://www.e-olymp.com/uk/submissions/7171196

def is_correct(length, array, k):
    ropes = 0

    for l in array:
        ropes += (l // length)

    return ropes >= k

def binary_search(array, k):
    left = 0
    right = max(array) + 1

    while right - left != 1:
        mid = left + (right - left) // 2

        if is_correct(mid, array, k):
            left = mid
        else:
            right = mid

    return left

if __name__ == '__main__':
    n, k = map(int, input().split())
    array = [int(input()) for i in range(n)]
    print(binary_search(array, k))