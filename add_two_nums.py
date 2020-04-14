# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-08 17:05:47
LastEditors: jiaqianjing
LastEditTime: 2020-04-08 17:52:32
"""

"""
leetcode 2: Add Two Numbers
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def add_two_nums(self, l1, l2):
        # 初始化一个链表 node，记录结果, head 是头节点
        head = ListNode(0)
        node = head
        # 进位标志位
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            _sum = x + y + carry
            carry = _sum // 10  # 进位要么 0， 要么 1
            node.next = ListNode(_sum % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            node = node.next
        
        if carry != 0:
            node.next = ListNode(1)
        return head.next

def print_list_node(l_head):
    res = []
    while l_head:
        res.append(str(l_head.val))
        l_head = l_head.next
    return "->".join(res)

    
# l1: (2 -> 4 -> 3) 
# l2: (5 -> 6 -> 4)
l1_head = ListNode(2)
l1 = l1_head
l1.next = ListNode(4)
l1 = l1.next
l1.next = ListNode(3)

l2_head = ListNode(5)
l2 = l2_head
l2.next = ListNode(6)
l2 = l2.next
l2.next = ListNode(4)

print("l1 node: {}".format(print_list_node(l1_head)))
print("l2 node: {}".format(print_list_node(l2_head)))

s = Solution()
res_node = s.add_two_nums(l1_head, l2_head)
print("res_node: {}".format(print_list_node(res_node)))





