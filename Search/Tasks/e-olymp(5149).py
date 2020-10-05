#https://www.e-olymp.com/uk/submissions/7171129

def is_correct(dist, coords, k):
    cows = 1
    prev = array[0]

    for c in coords[1:]:
        if c - prev >= dist:
            cows += 1
            prev = c

    return cows >= k

def binary_search(array, k):
    left = 0
    right = array[-1] - array[0] + 1

    while right - left != 1:
        mid = (left + right) // 2

        if is_correct(mid, array, k):
            left = mid
        else:
            right = mid

    return left

if __name__ == '__main__':
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(binary_search(array, k))