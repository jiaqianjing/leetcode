# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-14 14:45:09
LastEditors: jiaqianjing
LastEditTime: 2020-04-14 15:53:37
"""

"""
leetcode 64. 最小路径和 [动态规划]
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
    输入:
    [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # 当 row=0, 向下走，遍历第一列
        for col in range(1, cols):
            dp[0][col] = dp[0][col-1] + grid[0][col]

        # 当 col=0, 向右走，遍历第一行
        for row in range(1, rows):
            dp[row][0] = dp[row-1][0] + grid[row][0]

        # row > 0, col > 0
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]

        return dp[rows-1][cols-1]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
s = Solution()
res = s.minPathSum(grid)
print("res: {}".format(res))