class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_leftmost(array, x):
            left = 0
            right = len(array)

            while left < right:
                mid = (left + right) // 2

                if array[mid] < x:
                    left = mid + 1
                else:
                    right = mid

            return left

        def binary_rightmost(array, x):
            left = 0
            right = len(array)

            while left < right:
                mid = (left + right) // 2

                if array[mid] <= x:
                    left = mid + 1
                else:
                    right = mid

            return left - 1

        left = binary_leftmost(nums, target)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = binary_rightmost(nums, target)

        return [left, right]

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([3,5,6,9,12,23,33], 13))