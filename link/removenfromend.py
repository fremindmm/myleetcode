# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if head == None:
            return None
        if head.next == None:
            return None
        if head.next.next == None:
            if n == 1:
                return ListNode(head.val)
            elif n == 2:
                return ListNode(head.next.val)
            else:
                return None
        
        h = ListNode(-1)
        h.next = head
        pre, cur = h, h
        
        for _ in xrange(n+1):
            cur = cur.next
        while cur != None:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next
        return h.next
