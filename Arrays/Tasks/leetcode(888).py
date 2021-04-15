"""
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy
that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.
Since they are friends, they would like to exchange one candy bar each so that
after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange,
and ans[1] is the size of the candy bar that Bob must exchange.
If there are multiple answers, you may return any one of them.
It is guaranteed an answer exists.
Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
"""

class Solution:
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)

        for x in A:
            if (x + (Sb - Sa) // 2) in setB:
                return [x, x + (Sb - Sa) // 2]

if __name__ == '__main__':
    s = Solution()
    print(s.fairCandySwap([1, 2, 5],[2,4]))