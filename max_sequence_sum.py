# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-01 11:27:42
LastEditors: jiaqianjing
LastEditTime: 2020-04-03 18:21:22
"""


class Solution:
    def max_sequence_sum(self, nums):
        if len(nums) == 1:
            return nums[0]

        add_sum = 0
        # 负无穷
        max_sum = float("-inf")

        for index, val in enumerate(nums):
            temp = add_sum + nums[index]
            if temp >= nums[index]:
                add_sum = temp
            else:
                add_sum = nums[index]
            if max_sum < add_sum:
                max_sum = add_sum

        return max_sum


a = [4, 5, -1, -9, -17, 8, -18]
s = Solution()
res = s.max_sequence_sum(a)
print("raw nums: {}, max sequence sum: {}".format(a, res))


class Solution:
    def max_sum(self, nums):
        if len(nums) == 1:
            return nums
        
        add_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            temp = add_sum + nums[i]
            if temp >= nums[i]:
                add_sum = temp
            else:
                add_sum = nums[i]
        
        if max_sum < add_sum:
            max_sum = add_sum
        return max_sum



def max_sum(nums):
    if len(nums) == 1:
        return nums[0]
    add_sum = 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        temp = add_sum + nums[i]
        if temp >= nums[i]:
            add_sum = temp
        else:
            add_sum = nums[i]
        
        if max_sum < add_sum:
            max_sum = add_sum
    return max_sum
