#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/12/13 下午2:46
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : hasCycle.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
