class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        i = 1

        while i < len(flowerbed) - 1 and n:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                i += 2
            else:
                i += 1

        return n == 0

if __name__ == '__main__':
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1,0,0], 2))
