class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = 1000000000
        min2 = 1000000000
        max1 = -1000000000
        max2 = -1000000000
        max3 = -1000000000

        for i in range(len(nums)):
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]

            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max3 = max2
                max2 = nums[i]
            elif nums[i] > max3:
                max3 = nums[i]

        return max(max1 * max2 * max3, min1 * min2 * max1)

if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([1,2,3,4]))
