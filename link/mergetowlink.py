#!/bin/env python 

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        newList = None
        if l1.val < l2.val:
            newList = l1
            newList.next = self.mergeTwoLists(l1.next,l2)
        else:
            newList = l2
            newList = self.mergeTwoLists(l1, l2.next)
        return newList


class Solution12improve(object):
    def mergeTwoLists(self, l1, l2):
        top_node = None
        last_node = None
        while l1 or l2: 
            if l1 == None:
                val = l2.val
                l2 = l2.next
            elif l2 == None:
                val = l1.val
                l1 = l1.next
            elif l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            if last_node == None:
                top_node = ListNode(val)
                last_node = top_node
            else:
                last_node.next = ListNode(val)
                last_node = last_node.next
        return top_node

class Solutionfast(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        origin = ListNode(0)
        cur = origin
        while l2 is not None:
            while l1 is not None and l2.val > l1.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            cur.next = l2
            cur = cur.next
            l2 = l2.next
        cur.next = l1 if l2 is None else l2
        return origin.next

