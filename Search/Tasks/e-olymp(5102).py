#https://www.e-olymp.com/uk/submissions/7171004

def binary_search(n, x, y):
    x, y = min(x, y), max(x, y)
    left = 0
    right = (n - 1) * y

    while left < right:
        mid = (left + right) // 2
        k = mid // x + mid // y

        if k < n - 1:
            left = mid + 1
        else:
            right = mid

    return left + x

if __name__ == '__main__':
    n, x, y = map(int, input().split())
    print(binary_search(n, x, y))