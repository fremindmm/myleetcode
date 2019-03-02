#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/12/29 上午10:06
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : issymmetric.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.checkTwoTree(root.left, root.right)

    def checkTwoTree(self, leftTree, rightTree):
        if leftTree == None and rightTree == None:
            return True
        if leftTree != None and rightTree == None:
            return False
        if leftTree == None and rightTree != None:
            return False
        if leftTree.val != rightTree.val:
            return False
        left = self.checkTwoTree(leftTree.left, rightTree.right)
        right = self.checkTwoTree(leftTree.right, rightTree.left)
        return left and right


class Solution2(object):
    def isSymmetric(self, root):
        def issametree(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return issametree(l.left, r.right) and issametree(l.right, r.left)
            else:
                return False

        if not root:
            return True
        return issametree(root.left, root.right)


class Solution3(object):
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isSymmetric_2(root.left, root.right)

    def isSymmetric_2(self, left_root, right_root):
        if left_root == None and right_root != None:
            return False
        if left_root != None and right_root == None:
            return False
        if left_root == None and right_root == None:
            return True
        if left_root.val == right_root.val:
            if self.isSymmetric_2(left_root.left, right_root.right) and self.isSymmetric_2(left_root.right,
                                                                                           right_root.left):
                return True
        return False

        if root == None:
            return True
        res = self.isSymmetric_2(root.left, root.right)
        return res

    def isSymmetric_2(self, left_root, right_root):
        if left_root == None and right_root != None:
            return False
        if left_root != None and right_root == None:
            return False
        if left_root == None and right_root == None:
            return True
        if left_root.val == right_root.val:
            if self.isSymmetric_2(left_root.left, right_root.right) and self.isSymmetric_2(left_root.right,
                                                                                           right_root.left):
                return True
        return False


class Solution3(object):
    def isSymmetric(self, root):
        if not root:
            return True
        nodeList = [root.left, root.right]
        while nodeList:
            symmetricLeft = nodeList.pop(0)
            symmetricRight = nodeList.pop(0)
            if not symmetricLeft and not symmetricRight:
                continue
            if not symmetricLeft or not symmetricRight:
                return False
            if symmetricLeft.val != symmetricRight.val:
                return False
            nodeList.append(symmetricLeft.left)
            nodeList.append(symmetricRight.right)
            nodeList.append(symmetricLeft.right)
            nodeList.append(symmetricRight.left)
        return True

    def isSymmetric(self, root):
        if not root:
            return True
        nodeList = [root.left, root.right]
        while nodeList:
            symmetricLeft = nodeList.pop(0)
            symmetricRight = nodeList.pop(0)
            if not symmetricLeft and not symmetricRight:
                continue
            if not symmetricLeft or not symmetricRight:
                return False
            if symmetricLeft.val != symmetricRight.val:
                return False
            nodeList.append(symmetricLeft.left)
            nodeList.append(symmetricRight.right)
            nodeList.append(symmetricLeft.right)
            nodeList.append(symmetricRight.left)
        return True


class Solutionmy_recursive(object)
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmetric_2(root.left, root.right)

    def isSymmetric_2(self, rootLeft, rootRight):
        if rootLeft == None and rootRight != None:
            return False
        if rootLeft != None and rootRight == None:
            return False
        if rootLeft == None and rootRight == None:
            return True
        if rootLeft.val == rootRight:
            if self.isSymmetric_2(rootLeft.left, rootRight.right) and self.isSymmetric_2(rootLeft.right, rootRight.left):
                return True
        return False

class Soluthon_for(object):
    def isSmmetric(self,root):
        if root is None:
            return True
        node_list = [root.left, root.right]
        while node_list:
            symmetricLeft = node_list.pop(0)
            symmetricRight = node_list.pop(0)
            if not symmetricRight and not symmetricLeft:
                continue
            if not symmetricLeft or not symmetricRight:
                return False
            if symmetricRight.val == symmetricLeft.val:
                return False
            node_list.append(symmetricLeft.left)
            node_list.append(symmetricRight.right)
            node_list.append(symmetricLeft.right)
            node_list.append(symmetricRight.left)
        return True



