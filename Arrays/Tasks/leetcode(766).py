"""
Given an m x n matrix, return true if the matrix
is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left
to bottom-right has the same elements.

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
"""


class Solution:
    def isToeplitzMatrix(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i - 1][j - 1] != matrix[i][j]:
                    return False
        return True


class Solution1:
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if not r - c in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(s.isToeplitzMatrix([[1,2],[2,2]]))