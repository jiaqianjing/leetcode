# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-22 16:02:00
LastEditors: jiaqianjing
LastEditTime: 2020-04-23 11:10:23
"""

"""
leetcode 199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
输入: [1,2,3,null,5]
输出: [1, 3, 5]
解释:

   1            <---
 /   \
2     3         <---
 \     
  5             <---

"""

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

import collections
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def bfs(root):
            res_dict = {}

            # 双边队列，deque 数据类型来自于 collections 模块，支持从头和尾部的常数时间 append/pop 操作。
            # 若使用 Python 的 list，通过 list.pop(0) 去除头部会消耗 O(n)O(n) 的时间。
            queue = collections.deque([(root, 0)])
            while queue:
                # 从左到右遍历每一层的节点
                node, depth = queue.popleft()
                if node:
                    # 由于每一层最右边的节点才是我们要的答案，
                    # 因此不断更新对应深度的信息即可
                    res_dict[depth] = node.val
        
                    queue.append((node.left, depth+1))
                    queue.append((node.right, depth+1))

            return res_dict.values()

        def dfs(root):
            res_dict = {}

            stack = [(root, 0)]

            while stack:
                node, depth = stack.pop()
                if node:
                    # 只记录每一层最右边节点
                    res_dict.setdefault(depth, node.val)

                    stack.append((node.left, depth+1))
                    stack.append((node.right, depth+1))
            return res_dict.values()

        return bfs(root)


"""
       5
      / \
     3   6
    / \
   2   4
  /
 1
"""
root_node = TreeNode(5, left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)), right=TreeNode(6))

s = Solution()
res = s.rightSideView(root_node)
print("res: {}".format(res))
