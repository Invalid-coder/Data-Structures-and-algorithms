"""
Given n pairs of parentheses, write a function to
generate all combinations of well-formed parentheses.

Example 1:s

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


class Solution:
    def generateParenthesis(self, n):
        ans = []
        def _generateParenthesis(braces):
            if len(braces) == 2 * n:
                if not braces in ans:
                    ans.append(braces)
                return
            for i in range(len(braces)):
                _generateParenthesis(braces[:i] + "()" + braces[i:])
        _generateParenthesis("()")
        return ans

    def generateParenthesis1(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis1(c):
                for right in self.generateParenthesis1(N - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))