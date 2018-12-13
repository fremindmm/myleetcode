#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/12/4 上午10:35
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : reverseLink.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is  None or head.next is None:
            return head

        p = head
        q = head.next
        head.next = None
        while (q):
            r = q.next #r后移
            q.next = p #p q 交替反向
            p = q #快慢指针后移
            q = r

        head = p #q 必然指向是None
        return head

class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last

class Solution3(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur,pre = head,None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre



ActList * ReverseList2(ActList * head)
{
// ActList * temp = new
ActList;
if (NULL == head | | NULL == head->next)
return head; // 少于两个节点没有反转的必要。
ActList * p;
ActList * q;
ActList * r;
p = head;
q = head->next;
head->next = NULL; // 旧的头指针是新的尾指针，next需要指向NULL
while (q){
r = q->next; // 先保留下一个step要处理的指针
q->next = p; // 然后p q交替工作进行反向
p = q;
q = r;
}
head = p; // 最后q必然指向NULL，所以返回了p作为新的头指针
return head;
}
