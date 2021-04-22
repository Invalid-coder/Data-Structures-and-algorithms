"""
Write a function to find the longest common prefix
string amongst an array of strings.
If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
class Solution1:
    def longestCommonPrefix(self, words):
        if not words:
            return ""
        return self._longestCommonPrefix(words, 0, len(words) - 1 )

    def _longestCommonPrefix(self, words, left, right):
        if left == right:
            return words[left]
        mid = (left + right) // 2
        lcpLeft = self._longestCommonPrefix(words, left, mid)
        lcpRight = self._longestCommonPrefix(words, mid + 1, right)
        return self.commonPrefix(lcpLeft, lcpRight)

    def commonPrefix(self, left, right):
        n = min(len(left), len(right))
        for i in range(n):
            if left[i] != right[i]:
                return left[:i]
        return left[:n]


class Solution2():
    def longestCommonPrefix(self, words):
        if not words:
            return ""
        for i in range(len(words[0])):
            char = words[0][i]
            for j in range(1, len(words)):
                if len(words[j]) == i or words[j][i] != char:
                    return words[0][:i]
        return words[0]

class Solution3:
    def longestCommonPrefix(self, words):
        if not words:
            return ""
        minLen = float('inf')
        for word in words:
            minLen = min(minLen, len(word))
        left = 1
        right = minLen

        while left <= right:
            mid = (left + right) // 2
            if self.isCommonPrefix(words, mid):
                left = mid + 1
            else:
                right = mid - 1
        return words[0][:(left + right) // 2]

    def isCommonPrefix(self, words, minLen):
        prefix = words[0][:minLen]
        for i in range(1, len(words)):
            if not words[i].startswith(prefix):
                return False
        return True


class Node():
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord


class Solution4:
    def __init__(self):
        self.root = None

    def build(self, words):
        self.root = Node({}, False)
        for word in words:
            current = self.root
            for char in word:
                if not char in current.children:
                    current.children[char] = Node({}, False)
                current = current.children[char]
            current.isWord = True

    def longestCommonPrefix(self, words):
        self.build(words)
        prefix = ""
        current = self.root
        for i, char in enumerate(words[0]):
            if len(current.children) == 1 and not current.isWord:
                current = current.children[char]
                prefix += char
            else:
                return prefix
        return prefix


if __name__ == '__main__':
    s = Solution4()
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["ab", "a"]))
