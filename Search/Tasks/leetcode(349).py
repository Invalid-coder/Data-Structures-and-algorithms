"""

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""


class Solution:
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        if len(s1) < len(s2):
            return [x for x in s1 if x in s2]
        else:
            return [x for x in s2 if x in s1]

    def intersection(self, nums1, nums2):
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        return list(nums1 & nums2)

    
if __name__ == '__main__':
    s = Solution()
    print(s.intersection([4,9,5], [9,4,9,8,4]))

