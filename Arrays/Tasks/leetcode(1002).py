"""
Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings
within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.
You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""
import collections

class Solution():
    def commonChars(self, A):
        chars = []
        for c in A[0]:
            if c in chars:
                continue
            all_in = True
            counts = A[0].count(c)
            for word in A[1:]:
                if not c in word:
                    all_in = False
                    break
                else:
                    counts = min(counts, word.count(c))

            if all_in:
                for _ in range(counts):
                    chars.append(c)
        return chars

    def commonChars1(self, A):
        c = collections.Counter(A[0])
        for i in range(1, len(A)):
            c &= collections.Counter(A[i])
        return list(c.elements())

if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["bella","label","roller"]))