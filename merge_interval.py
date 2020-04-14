# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-08 11:05:51
LastEditors: jiaqianjing
LastEditTime: 2020-04-12 12:27:19
"""

"""
leetcode 56 合并间隔区间: 给出一个区间的集合，请合并所有重叠的区间。
Given a collection of intervals, merge all overlappingintervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []
        intervals.sort()
        begin = intervals[0][0]
        end = intervals[0][1]
        print("after sort list: {}".format(intervals))
        print("begin: {}, end: {}".format(begin, end))
        # 创建一个 list 记录遍历的结果
        res = list()
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                # no ovlerlapping intervals of collections
                res.append([begin, end])
                # 重新赋值新的起始边界
                begin = intervals[i][0]
                end = intervals[i][1]
            else:
                # 有重叠区间
                if intervals[i][1] > end:
                    end = intervals[i][1]
        res.append([begin, end])
        return res

l = [[11, 19], [1, 3], [2, 5], [8, 10]]
print("raw collections: {}".format(l))
s = Solution()
l_ = s.merge(l)
print("collections: {}".format(l_))


