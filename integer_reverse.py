# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-14 12:14:33
LastEditors: jiaqianjing
LastEditTime: 2020-04-14 17:06:56
"""

"""
leetcode 7: Reverse Integer
Example 1:
    Input: 123
    Output: 321

Example 2:
    Input: -123
    Output: -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        res = int(str(abs(x))[::-1]) * flag
        # 判断 revert 后的数字是否在整数范围内 (-2^31, 2^31-1)
        if -2 ** 31 < res < 2 ** 31 -1:
            return res
        else:
            return 0

s = Solution()
test = -123
res = s.reverse(test) 
print("raw test: {}, reverse: {}".format(test, res))

