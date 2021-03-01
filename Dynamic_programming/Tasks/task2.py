"""
Given a rectangular field of n * m cells.
You can take one-square steps to the right, down, or diagonally right and down.
Each cell contains some natural number.
It is necessary to get from the upper left cell to the lower right one.
Route weight is calculated as the sum of numbers from all visited cells.
It is necessary to find the route with the minimum weight.
"""
di = [0, -1, -1]
dj = [-1, 0, -1]

if __name__ == '__main__':
    n = int(input("n = "))
    A = [list(map(int, input().split())) for i in range(n)]
    m = len(A[0])
    W = [[float("Inf") for i in range(m)] for i in range(n)]
    W[0][0] = A[0][0]
    mapping = {(0, 0): None}

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i - 1 > -1 and j - 1 > -1:
                W[i][j] = min(W[i - 1][j], W[i][j - 1], W[i - 1][j - 1])
                mapping[(i, j)] = min([(i - 1, j), (i, j - 1), (i - 1, j - 1)], key=lambda pos: W[pos[0]][pos[1]])
            else:
                W[i][j] = W[i - 1][j] if i - 1 > -1 else W[i][j - 1]
                mapping[(i, j)] = (i - 1, j) if i - 1 > -1 else (i, j - 1)

            W[i][j] += A[i][j]

    stack = []
    current = (n - 1, m - 1)

    while current:
        stack.append(current)
        current = mapping[current]

    way = []

    while stack:
        way.append(stack.pop())

    print(way)
    print(W[n - 1][m - 1])