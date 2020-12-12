"""
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?



Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_row = [1]
        curr_row = [1]

        for row_num in range(1, rowIndex + 1):
            curr_row = [None for _ in range(row_num + 1)]
            curr_row[0], curr_row[-1] = 1, 1

            for i in range(1, len(curr_row) - 1):
                curr_row[i] = prev_row[i - 1] + prev_row[i]

            prev_row = curr_row

        return curr_row

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))