#!/bin/bash
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#[3,9,20,null,null,15,7],

#按层输出
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root is None:
            return rest
        q = []
        q.append(root)
        while len(q) != 0:
            tmp = []
            length = len(q)
            for i in range(length):
                r = q.pop(0)
                if r.left is not None:
                    q.append(r.left)
                if r.right is not None:
                    q.append(r.right)
                tmp.append(r.val)
            res.append(tmp)   
         return res


class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result
        
        q = []
        q.append(root)
        while len(q) != 0:
            level = []
            l = len(q)
            for i in xrange(l):
                node = q.pop(0)
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(level)
        return result

#按层遍历
class Solution3(object):
      def levelOrder(self, root):
        outList=[]
        queue=[root]
        while queue!=[] and root:
            outList.append(queue[0].val)      
            if queue[0].left!=None:
                queue.append(queue[0].left)
            if queue[0].right!=None:
                queue.append(queue[0].right)
            queue.pop(0)
        return outList
        outList = []

class Solution4(object):
      def levelOrder(self, root):
          if not root:
              return []
          currentStack = [root]
          outList = []
          while currentStack:
              nextStack = []
              for point in currentStack:
                  if point.left:
                       nextStack.append(point.left)
                  if point.right:
                       nextStack.append(point.right)
                  outList.append(point.val)
              currentStack = nextStack
          return outList
 



