#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/12/25 上午10:25
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : binarysearchtree.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inorderTraversal(root):
            if root == None:
                return []
            res = []
            res += inorderTraversal(root.left)
            res.append(root.val)
            res += inorderTraversal(root.right)
            return res

        res = inorderTraversal(root)
        if res != sorted(list(set(res))):
            return False
        return True

class Solution2(object):
    def isValidBST(self, root):
        return self.helper(root, -1 << 63, (1 << 63) - 1)

    def helper(self, root, minVal, maxVal):
        if root:
            if not minVal < root.val < maxVal:
                return False

            return self.helper(root.left, minVal, root.val) and self.helper(root.right, root.val, maxVal)
        return True

class Solution3(object):
    def ValidBST(self, root, small, large):
        if root == None:
            return True
        elif small >= root.val or large <= root.val:
            return False

        return self.ValidBST(root.left, small, root.val) and self.ValidBST(root.right, root.val, large)

    def isValidBST(self, root):

        return self.ValidBST(root, -20000000000000000, 20000000000000000)