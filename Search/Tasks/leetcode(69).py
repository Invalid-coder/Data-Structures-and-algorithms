"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since the decimal part is truncated, 2 is returned.
"""

class Solution:
    def mySqrt(self, x):
        if not x:
            return 0
        if x <= 3:
            return 1
        left, right = 1, x // 2
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
                ans = mid
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return ans
