"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-03-01 11:53:13
LastEditors: jiaqianjing
LastEditTime: 2020-03-01 11:59:05
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

        temp_list.sort()

        new_list_node = ListNode(temp_list[0])
        new_list_head = new_list_node

        for i range(1, len(temp_list)):
            new_list_node.next = temp_list[i]
            new_list_node = new_list_node.next
        
        new_list_node.next = None
        return new_list_head
