class Solution:
    def findWaysAmount(self, s, k):
        return self._countSplittings(s, k)

    def _getCounts(self, s, k):
        return s.count('1')

    def _countSplittings(self, s, k):
        count = 0
        for index in range(k, len(s) + 1):
            prefix = s[:index]
            suffix = s[index:]
            counts = self._getCounts(prefix, k)
            if counts == k:
                if suffix:
                    count += self._countSplittings(suffix, k)
                else:
                    count += 1
            elif counts > k:
                return count
        return count

# Write your code here
t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    S = input()
    s = Solution()
    res = s.findWaysAmount(S, K)
    print(res if res > 0 else -1)
