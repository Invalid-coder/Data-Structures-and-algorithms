"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
"""


class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary1(self, a, b):
        carry = False
        a = a[::-1]
        b = b[::-1]
        a, b = sorted([a, b], key=lambda x: len(x))
        ans = ''
        i = 0
        while i < len(a):
            if a[i] == b[i] and a[i] == '1':
                if carry:
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                    carry = True
            elif a[i] == b[i] and a[i] == '0':
                if carry:
                    ans = '1' + ans
                    carry = False
                else:
                    ans = '0' + ans
            else:
                if carry:
                    ans = '0' + ans
                else:
                    ans = '1' + ans
            i += 1
        while i < len(b):
            if carry:
                if b[i] == '1':
                    ans = '0' + ans
                elif b[i] == '0':
                    ans = '1' + ans
                    carry = False
            else:
                ans = b[i] + ans
            i += 1
        if carry:
            ans = '1' + ans
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("1010", "1011"))