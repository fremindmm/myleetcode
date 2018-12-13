#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/12/12 下午4:46
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : isPalindRome.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middle(self, string):
        return string[1:-1]

    def isPalindromes(self, string):
        if string[0] is not string[-1]:
            return False
        elif len(string) == 0 or len(string) == 1:
            return True
        else:
            return self.isPalindromes(self.middle(string))

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        else:
            cur = head
            lit = []
            while cur:
                lit.append(cur.val)
                cur = cur.next
            return lit == lit[::-1]


class Solution2(object):
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
