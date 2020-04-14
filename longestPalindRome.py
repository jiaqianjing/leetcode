# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-01 11:59:57
LastEditors: jiaqianjing
LastEditTime: 2020-04-09 23:32:07
"""

"""
leetcode 5: 最长回文子串
"""
class Solution:
    def force(self, s):
        """
        暴力求解
        """
        if s==s[::-1]:
            return s
        max_len = 1
        res = s[0]
        print(res)
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j - i + 1
                    res = s[i:i + max_len]
        return res


    def longestPalindaRome(self, s):
        """
        动态规划
        """
        start_index = 0
        max_len = 0
        for i in range(len(s)):
            while i - max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start_index = i - max_len - 1
                max_len = max_len + 2
                continue
            while i - max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start_index = i - max_len
                max_len = max_len + 1
        return s[start_index:start_index+max_len]


test_01 = "abccbdabccba33kdk"
test_02 = "ac"
s = Solution()
res_01 = s.longestPalindaRome(test_01)
print("test_01 raw string: {}, res_01: {}".format(test_01, res_01))
res_02 = s.force(test_02)
print("test_02 raw string: {}, res_02: {}".format(test_02, res_02))


