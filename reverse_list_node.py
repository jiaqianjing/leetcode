# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-10 10:43:27
LastEditors: jiaqianjing
LastEditTime: 2020-04-10 11:38:15
"""

"""
leetcode 24 反转链表
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverse_list(self, head):
        """
        双指针迭代
        """
        cur = head
        pre = None
        # 遍历待逆序的链表，每遍历一个节点，就将指针指向 pre，然后 pre 、cur 都前进一位
        while cur:
            # 暂存下个节点
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


def print_list_node(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print("->".join(res))
        
# 1->2->3->4->5->NULL
test_node_head = ListNode(1)
test_node = test_node_head
test_node.next = ListNode(2)
test_node = test_node_head.next
test_node.next = ListNode(3)
print("test_node_head: ")
print_list_node(test_node_head)
s = Solution()
res = s.reverse_list(test_node_head)
print("reverse test_node_head: ")
print_list_node(res)




