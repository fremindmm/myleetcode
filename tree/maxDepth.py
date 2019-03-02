#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/12/24 上午11:17
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : maxDepth.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int  97%
        """
        if not root:
            return 0
        if root.left is None:
            return self.maxDepth(root.right) + 1
        if root.right is None:
            return self.maxDepth(root.left) + 1

        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution(object):
        def maxDepth(self, root):
            if not root:
                return 0
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


