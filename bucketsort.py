"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-01 10:54:30
LastEditors: jiaqianjing
LastEditTime: 2020-04-10 12:44:17
"""
class Solution:
    def bucket_sort(self, nums):
        bucket = [0] * 11
        for i in nums:
            bucket[i] += 1
        result = []
        for index, val in enumerate(bucket):
            if val > 0:
                for k in range(val):
                    result.append(index)
        return result

        
a = [2,3,6,1,2,2]
print("raw nums: {}".format(a))
s = Solution()
res = s.bucket_sort(a)
print("bucket sort: {}".format(res))


            