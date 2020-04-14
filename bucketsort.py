"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-01 10:54:30
LastEditors: jiaqianjing
LastEditTime: 2020-04-14 14:05:12
"""
class Solution:
    def bucket_sort(self, nums):
        if not nums:
            return []
        bucket = [0] * 11
        for i in nums:
            bucket[i] += 1
        res = []
        for index, val in enumerate(bucket):
            if val >= 1:
                for _ in range(val):
                    res.append(index)
        return res

        
a = [2,3,6,1,2,2]
print("raw nums: {}".format(a))
s = Solution()
res = s.bucket_sort(a)
print("bucket sort: {}".format(res))

