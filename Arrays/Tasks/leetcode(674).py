"""
Given an unsorted array of integers nums,
return the length of the longest continuous increasing subsequence (i.e. subarray).
The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r)
such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]
and for each l <= i < r, nums[i] < nums[i + 1].

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence,
it is not continuous as elements 5 and 7 are separated by element
4.
"""

class Solution:
    def findLengthOfLCIS(self, nums):
        left = 0
        max_length = 0

        while left < len(nums):
            right = left + 1
            while right < len(nums) and nums[right] > nums[right - 1]:
                right += 1
            max_length = max(max_length, right - left)
            left = right

        return max_length

if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([1,3,5,4,7]))