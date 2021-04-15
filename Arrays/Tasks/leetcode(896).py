"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
"""

def get_comparison(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

class Solution:
    def isMonotonic(self, A):
        """
            One pass
        """

        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                increasing = False
            if A[i] < A[i + 1]:
                decreasing = False

        return increasing or decreasing


    def isMonotonic1(self, A):
        """
            One pass
        """
        store = 0

        for i in range(len(A) - 1):
            c = get_comparison(A[i], A[i + 1])

            if c:
                if c != store != 0:
                    return False

                store = c

        return True


    def isMonotonic(self, A):
        """
            Two passes
        """
        increasing = decreasing = True

        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                increasing = False
                break

        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                decreasing = False
                break

        return increasing or decreasing


if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic1([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]))

