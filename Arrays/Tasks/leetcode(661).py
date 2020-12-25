class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R = len(M)
        C = len(M[0])
        ans = [[0] * C for i in range(R)]

        for r in range(R):
            for c in range(C):
                counter = 0

                for i in (r - 1, r, r + 1):
                    for j in (c - 1, c, c + 1):
                        if 0 <= i < R and 0 <= j < C:
                            ans[r][c] += M[i][j]
                            counter += 1

                ans[r][c] /= counter

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))