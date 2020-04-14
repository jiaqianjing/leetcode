"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-01 10:37:26
LastEditors: jiaqianjing
LastEditTime: 2020-04-03 18:59:18
"""


class Solution:
    def merge_sort(self, nums):
        def _merge(left, right):
            i = 0
            j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

                if i == len(left):
                    result.extend(right[j:])
                elif j == len(right):
                    result.extend(left[i:])
            return result

        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return _merge(left, right)


s = Solution()
a = [4, 2, 2, 2, 9, 5, 9, 3, 4, 5, 6]
print("raw nums: {}".format(a))
res = s.merge_sort(a)
print("merge sort: {}".format(res))

class Solution:
    def merge_sort(self, nums):
        def merge(left, right):
            i = 0
            j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                
                if i == len(left):
                    result.extend(right[j:])
                elif j == len(right):
                    result.extend(left[i:])
            return result
                    


    
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return merge(left, right)

    
    
    class Solution:
        def merge_sort(self, nums):
            def merge(left, right):
                i = 0
                j = 0
                result = []
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        result.append(left[i])
                    
            
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left = self.merge_sort(nums[:mid])
            right = self.merge_sort(nums[mid:])

            return merge(left, right)

        