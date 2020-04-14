"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-01 11:53:13
LastEditors: jiaqianjing
LastEditTime: 2020-04-14 13:51:23
"""
class ListNode:
    def __init__(self, val)
        self.val = val
        self.next = None

class Solution:
    def merge_two_list_node(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        else l1 is None and l2 is not None:
            return l2
        else l1 is not None and l2 is None:
            return l1

        temp_list = []
        while l1:
            temp_list.append(l1.val)
            l1 = l1.next
        
        while l2:
            temp_list.append(l2.val)
            l2 = l2.next
        # 排序
        temp_list.sort()

        # 创建一个新链表存放结果
        head = ListNode(0)
        node = head
        for i in temp_list:
            node.next = ListNode(i)
            node = node.next
        
        return head.next
