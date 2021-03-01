"""
The chess knight stands in cell (1, 1) on a board of size N x M.
It is required to calculate the number of ways to get to cell (N, M)
by moving by four types of steps. (2, -1), (2, 1), (-1, 2), (1, 2)
"""

def ways(i, j):
    if i < 0 or j < 0 or i > n - 1 or j > m - 1:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = ways(i - 2, j - 1) + ways(i - 2, j + 1) + ways(i - 1, j - 2) + ways(i + 1, j - 2)
    return dp[i][j]

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    dp = [[-1 for j in range(m)] for i in range(n)]
    dp[0][0] = 1
    print(ways(n - 1, m - 1))
    print(dp)