# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-01 11:08:19
LastEditors: jiaqianjing
LastEditTime: 2020-04-14 09:59:03
"""
class Solution:
    def two_sum_01(self, nums, target):
        i = 0
        while i < len(nums):
            temp = target - nums[i]
            follows = nums[i+1:]
            if temp in follows:
                return [i, follows.index(temp) + i + 1]
            i += 1
        return "no solution"

    def two_sum_02(self, nums, target):
        """
        构造字典
        """
        if len(nums) == 1:
            return nums[0]
        my_dict = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in my_dict.keys():
                return [i, my_dict[temp]]
            else:
                my_dict[nums[i]] = i




target=5
a = [2,3,1]
s = Solution()
res = s.two_sum_01(a, target)
print("way 01: raw nums: {}, taget: {}, res: {}".format(a, target, res))
res = s.two_sum_02(a, target)
print("way 02: raw nums: {}, taget: {}, res: {}".format(a, target, res))
