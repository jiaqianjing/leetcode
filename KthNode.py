# coding:utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-10 17:12:34
LastEditors: jiaqianjing
LastEditTime: 2020-04-03 17:56:05
"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    """
    leetcode230: 二叉搜索树中第 K 小的元素
    给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
    """

    def KthSmallest_01(self, root, k):
        """
        时间复杂度： O(N)
        空间复杂度：O(N)
        """
        def inorder(root):
            """
            中序遍历
            """
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return inorder(root)[k-1]

    # 统计是否到了目标 k 值
    count = 0

    def KthSmallest_02(self, root, k):
        """
        时间复杂度: O(N)
        空间复杂度: O(1)
        """
        def find_k_node(root, k):
            if root is None:
                return None
            node = find_k_node(root.left, k)
            if node:
                return node
            self.count += 1
            if self.count == k:
                return root

            node = find_k_node(root.right, k)
            if node:
                return node
        return find_k_node(root, k).val


"""
       5
      / \
     3   6
    / \
   2   4
  /
 1
"""


def test():

    root_node = TreeNode(5, left=TreeNode(3, left=TreeNode(
        2, left=TreeNode(1)), right=TreeNode(4)), right=TreeNode(6))
    s = Solution()
    # res = s.KthSmallest_01(root_node, 4)
    res = s.KthSmallest_02(root_node, 4)
    print("res: {}".format(res))



class Solution_01:
    count = 0

    def KthSmallest_01(self, root, k):
        def find_k_node(root, k):
            if root is None:
                return None
            node = find_k_node(root.left, k)
            if node:
                return node
            
            self.count += 1
            if self.count == k:
                return root
            
            node = find_k_node(root.right, k)
            if node:
                return node

        return find_k_node(root, k).val

    def KthSmallest_02(self, root, k):
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return inorder(root)[k-1]


"""
       10
      / \
     5   11
    / \
   4   9
  /
 1
"""
test_node = TreeNode(10, TreeNode(5, TreeNode(4, TreeNode(1)), TreeNode(9)), TreeNode(11))
s = Solution_01()
res = s.KthSmallest_02(test_node, 4)
print(res)


class Solution:
    count = 0
    def KthSmallest(self, root, k):
        def find_k_node(root, k):
            if root is None:
                return None
            node = find_k_node(root.left, k)
            if node:
                return node
            self.count += 1
            if self.count == k:
                return root
            node = find_k_node(root.right, k)
            if node:
                return node
        return find_k_node(root, k).val

    def KthSmallest(self, root, k):
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return inorder(root)[k-1]
        
        
