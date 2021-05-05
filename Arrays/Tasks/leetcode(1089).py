"""
Given a fixed length array arr of integers, duplicate each occurrence of zero,
\shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        dups = 0
        n = len(arr) - 1
        for left in range(n + 1):
            if left > n - dups:
                break
            if arr[left] == 0:
                if left == n - dups:
                    arr[n] = 0
                    n -= 1
                    break
                dups += 1
        last = n - dups
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + dups] = 0
                dups -= 1
                arr[i + dups] = 0
            else:
                arr[i + dups] = arr[i]




if __name__ == '__main__':
    s = Solution()
    arr = [1,0,2,3,0,4,5,0]
    print(s.duplicateZeros(arr))
    print(arr)