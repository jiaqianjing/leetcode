# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-12 15:59:00
LastEditors: jiaqianjing
LastEditTime: 2020-04-12 20:55:17
"""

"""
leetcode 4: 寻找两个有序数组的中位数 （时间复杂度控制在 O (log (m+n))）
"""

class Solution:
    def find_median_num(self, nums1, nums2):
        """
        时间复杂度 > O(m+n), 因为涉及对数组排序了，但是此方法易懂
        中位数定义：将集合等分两部分，且一部分的最小值大于另一部分的最大值；假设有集合 N(1,2,3...,m)
            odd(基数)：median_num = N[(m+1)/2]
            even(偶数): median_num = (N[m/2] + N[m/2+1])/2
        [1,2,3] => median_num = 2
        [1,2,3,4] => median_num = (2+3) / 2 = 2.5
        """
        median_num = 0.0
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 0:
            # is even number
            # 因为 list index=0 开始，所以计算的下标值得 -1
            median_num = (float(nums1[len(nums1)/2 - 1]) + float(nums1[len(nums1)/2 + 1 - 1]))/2
            print("[even] median_num: {}".format(median_num))
        else:
            # is odd number
            median_num = float(nums1[(len(nums1) + 1)/2 - 1])
            print("[odd] median_num: {}".format(median_num))
        return median_num


test_01 = [1,2,3]
test_02 = [4]
s = Solution()
res = s.find_median_num(test_01, test_02)

print("res: {}".format(res))