def from_right_to_left(rows, cols, arr):
    for k in range(cols - 1):
        for j in range(k + 1):
            i = k - j
            print(arr[j][i], end=' ')
        print()

    for k in range(cols - 1):
        for j in range(k + 1):
            i = k - j
            print(arr[rows - j - 1][cols - i - 1], end=' ')
        print()


def from_left_to_right(rows, cols, arr):
    for k in range(rows - 1):#
        for j in range(k + 1):
            i = k - j
            print(arr[rows - i - 1][j], end=' ')
        print()

    for k in range(cols - 1):#
        for j in range(k + 1):
            i = k - j
            print(arr[j][cols - i - 1], end=' ')
        print()


def main_diagonals(rows, cols, arr):
    for i in range(rows):
        if i > cols - 1:
            break
        print(arr[i][i], end= ' ')
    print()
    for i in range(cols):
        if i > rows - 1:
            break
        print(arr[i][cols - i - 1], end=' ')
    print()


def mirrored(rows, cols, arr):
    for k in range(rows - 2, -1, -1):
        for j in range(k + 1):
            i = k - j
            print(arr[rows - i - 1][j], end=' ')
        print()

    for k in range(cols - 1):
        for j in range(k + 1):
            i = k - j
            print(arr[j][cols - i - 1], end=' ')
        print()

    for k in range(cols - 2, -1, -1):
        for j in range(k + 1):
            i = k - j
            print(arr[j][cols - i - 1], end=' ')
        print()

    for k in range(cols - 1):
        for j in range(k + 1):
            i = k - j
            print(arr[rows - j - 1][cols - i - 1], end=' ')
        print()

    for k in range(cols - 1):
        for j in range(k + 1):
            i = k - j
            print(arr[j][i], end=' ')
        print()

    for k in range(cols - 2, -1, -1):
        for j in range(k + 1):
            i = k - j
            print(arr[j][i], end=' ')
        print()

    for k in range(cols - 1):
        for j in range(k + 1):
            i = k - j
            print(arr[rows - j - 1][cols - i - 1], end=' ')
        print()

    for k in range(cols - 2, -1, -1):
        for j in range(k + 1):
            i = k - j
            print(arr[n - j - 1][m - i - 1], end=' ')
        print()


if __name__ == '__main__':
    n = int(input("n = "))
    arr = [list(map(int, input().split())) for _ in range(n)]
    m = len(arr[0])

    from_right_to_left(n, m, arr)
    print()
    from_left_to_right(n, m, arr)
    print()
    main_diagonals(n, m, arr)
    print()
    mirrored(n, m, arr)
