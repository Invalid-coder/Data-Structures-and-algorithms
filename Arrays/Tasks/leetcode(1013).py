"""
Given an array of integers arr, return true if we can partition
the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j
with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ...
+ arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])


Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
"""


class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3 != 0:
            return False
        v = total / 3
        times = 0
        total = 0
        for i in arr:
            total += i
            if total == v:
                total = 0
                times += 1
        return times >= 3




if __name__ == '__main__':
    s = Solution()
    print(s.canThreePartsEqualSum([18,12,-18,18,-19,-1,10,10]))
