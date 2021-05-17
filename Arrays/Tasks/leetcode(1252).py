"""
There is an m x n matrix that is initialized to all 0's.
There is also a 2D array indices where each indices[i] = [ri, ci]
represents a 0-indexed location to perform some increment operations on the matrix.
For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in
the matrix after applying the increment to all locations in indices.

Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
"""


class Solution:
    def oddCells(self, m, n, indices):
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        return sum([1 for r in range(m) for c in range(n) if (rows[r] + cols[c]) % 2 == 1])


    def oddCells1(self, m, n, indices):
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for r, c in indices:
            for j in range(n):
                matrix[r][j] += 1
            for i in range(m):
                matrix[i][c] += 1
        return sum([1 for i in range(m) for j in range(n) if matrix[i][j] % 2 == 1])

if __name__ == '__main__':
    s = Solution()
    print(s.oddCells(2, 3, [[0,1],[1,1]]))