class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_average = sum(nums[:k]) / k
        i = 0

        for j in range(k, len(nums) + 1):
            max_average = max(max_average, sum(nums[i:j]) / k)
            i += 1

        return max_average

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4))