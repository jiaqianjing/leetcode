"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-02-29 19:58:09
LastEditors: jiaqianjing
LastEditTime: 2020-04-03 18:50:22
"""


class Solution:
    def quick_sort(self, nums, low, high):
        def _partition(nums, low, high):
            pivot = nums[low]
            while low < high:
                while low < high and nums[high] >= pivot:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] < pivot:
                    low += 1
                nums[high] = nums[low]
            pivot = nums[low]
            return low

        if low >= high:
            return
        k = _partition(nums, low, high)
        self.quick_sort(nums, low, k)
        self.quick_sort(nums, k+1, high)


a = [1, 5, 2, 6, 6, 8]
print("raw nums: {}".format(a))
s = Solution()
s.quick_sort(a, 0, len(a)-1)
print("quick sort nums: {}".format(a))


class Soluition:
    def quick_sort(self, nums, low, high):
        def partion(nums, low, high):
            pivot = nums[low]
            while low < high:
                while low < high and nums[high] >= pivot:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] < pivot:
                    low += 1
                nums[high] = nums[low]
            pivot = nums[low]
            return low

        if low >= high:
            return
        
        k = partion(nums, low, high)
        self.quick_sort(nums, low, k):
        self.quick_sort(nums, k+1, high)



class Solution:
    def quick_sort(self, nums, low, high):
        def partion(nums, low, high):
            pivot = nums[low]
            while low < high:
                while low < high and nums[high] >= pivot:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] > pivot:
                    low += 1
                nums[high] = nums[low]
            pivot = nums[low]
            return low
        
        if low >= high:
            return
        
        k = partion(nums, low, hgih)
        self.quick_sort(nums, low, k)
        self.quick_sort(nums, k+1, high)