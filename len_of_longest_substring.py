# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-09 12:03:43
LastEditors: jiaqianjing
LastEditTime: 2020-04-10 14:15:45
"""
"""
leetcode 02: 无重复字符的最长子串
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
class Solution:
    def length_of_longest_sub_string(self, s):
        if not s:
            return 0
        left = 0
        windows = set()
        cur_len = 0
        max_len = 0
        for i in s:
            # 滑动窗口长度 +1
            cur_len += 1
            # foucus 不能用 if, 要确保滑动窗口内的所有元素不能重复
            while i in windows:
                windows.remove(s[left])
                left += 1
                cur_len -= 1
            if max_len < cur_len:
                max_len = cur_len
            windows.add(i)
        print("---> {}".format(windows))
        return max_len

test = "pwwkew"
s = Solution()
res = s.length_of_longest_sub_string(test)
print("res: {}".format(res))

