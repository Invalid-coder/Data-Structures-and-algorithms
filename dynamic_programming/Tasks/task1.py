"""
Given a rectangular field of n * m cells.
You can take one square steps to the right or down.
Calculate how many ways you can get from the upper left cell to the lower right.
"""

if __name__ == '__main__':
    n = int(input("n = "))
    m = int(input("m = "))
    A = [[0 for j in range(m)] for i in range(n)]
    A[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i - 1 > -1:
                A[i][j] += A[i - 1][j]
            if j - 1 > -1:
                A[i][j] += A[i][j - 1]

print(A[n - 1][m - 1])

