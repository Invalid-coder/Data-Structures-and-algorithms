"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars
(each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""


class Solution:
    def countCharacters(self, words, chars):
        dict1 = {}
        length = 0
        for c in chars:
            if not c in dict1:
                dict1[c] = 0
            dict1[c] += 1
        for word in words:
            dict2 = dict1.copy()
            formed = True
            for c in word:
                if c in dict2:
                    dict2[c] -= 1
                    if dict2[c] < 0:
                        formed = False
                        break
                else:
                    formed = False
                    break
            if formed:
                length += len(word)
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.countCharacters(["cat","bt","hat","tree"], "atach"))