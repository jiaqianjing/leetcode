# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-15 13:56:38
LastEditors: jiaqianjing
LastEditTime: 2020-04-15 15:37:53
"""

"""
leetcode 542. 01 矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

示例 1:
    输入:
        0 0 0
        0 1 0
        0 0 0
    
    输出:
        0 0 0
        0 1 0
        0 0 0

示例 2:
    输入:
        0 0 0
        0 1 0
        1 1 1
    
    输出:
        0 0 0
        0 1 0
        1 2 1
"""
import collections
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # 创建二维数组，存储结果
        dist = [[0] * cols for _ in range(rows)]
        # 记录 0 的坐标
        zeroes_pos = [(r, c) for r in range(rows) for c in range(cols) if matrix[r][c] == 0]
        # 将所有的 0 坐标添加进初始队列中 
        # deque (double-ended queue) --> 双边队列, 具有队列和栈的性质，在 list 的基础上增加了移动、旋转和增删等
        q = collections.deque(zeroes_pos)
        # 暂存当前已经遍历过点
        seen = set(zeroes_pos)

        # BFS (breadth first search)
        while q:
            row, col = q.popleft()
            # 上、下、左、右走一步，距离 +1；同时注意边界问题，以及是否走一步后是否是其他 0 点的坐标
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0<=r< rows and 0<=c< cols and (r, c) not in seen:
                    dist[r][c] = dist[row][col] + 1
                    q.append((r, c))
                    seen.add((r, c))
        return dist


test = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
   ]
s = Solution()
res = s.updateMatrix(test)
print("raw: {}".format(test))
print("update: {}".format(res))