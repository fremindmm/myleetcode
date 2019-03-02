"""解题思路：因为给定的数组是按照升序排列的，所以可以先取出数组中间位置的值作为二叉查找树的根结点，然后以该数组中间位置的值为中心，将左边的数组划分到根结点的左子树中，右边的数组划分到根结点的右子树中，这样就能保证根结点的左子树上任意结点的值都小于根结点的值，右子树上任意结点的值大于根节点的值。接下来，可以使用递归地方法继续取出左边数组的中间值作为根结点的左子结点，右边数组的中间值作为根结点的右子结点，然后以左边数组中间值为中心，再次划分左右子树，右边数组同理，如此递归下去，对于每个结点，总是能保证其左子树上任意结点的值都要小于该节点的值，其右子树上任意结点的值都要大于该节点的值
"""
        #递归方法
        if not nums:
            return None
        mid=len(nums)//2#找到中间节点
        root=TreeNode(nums[mid])#当前节点为根节点
        root.left=self.sortedArrayToBST(nums[:mid])#小于当前根节点的作为左子树
        root.right=self.sortedArrayToBST(nums[mid+1:])#大于当前根节点的作为右子树
        return root
#recursive
class Solutions(object):
    def sortedArray2BST(nums):
        if not nums:
            return None
        mid = len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.sortedArray2BST(nums[:mid])
        root.right=self.sortedArray2BST(nums[mid+1:])
        return root

class Solutions(object):
     def sortedArray2BST(nums):
         if not nums:
             return None
         mid = len(nums)//2
         root = TreeNode(nums[mid])
         root.left = self.sortedArrayToBST(nums[:mid])
         root.right = self.sortedArrayToBST(nums[mid+1:])
         return root
  



#递归如何转化成非递归
#recursive
class Solutions2(object):
    def sortedArray2BST(nums):
        return self.build(nums, 0, len(nums) - 1)
    def build(self, nums, left = None, right = None):
        if left > right:
            return None
        elif left == right:
            return TreeNode(nums[left])
        else:
            mid = (left + right) / 2
            left_node = self.build(nums, left, mid - 1)
            right_node = self.build(nums, mid + 1, right)
            tn = TreeNode(nums[mid])
            tn.left = left_node
            tn.right = right_node
            return tn

class solutions2(object):
    def sortedArrayToBTS(nums):
        return self.build(num, 0, len(nums)-1)
    def build(self, nums, left = None, right = None):
        if left > right:
            return None
        elif left == right:
            return TreeNode(nums[left])
        else:
            mid = (left + right) / 2
            left_node = self.build(nums, left, mid - 1)
            right_node = self.build(nums, mid + 1, right)
            tn = TreeNode(nums[mid])
            tn.left = left_node
            tn.right = right_node
            return tn
class solutions(object):
    def sortedArrayToBST(nums):
        return self.build(num, 0 , len(nums) -1 )
    def build(self, nums, left=None, right=None):
        if left > right:
            return None:
        else left == right:
            return TreeNode(nums[left])
        else:
             mid = (left + right) / 2
             left_node = self.build(nums, left, mid-1)
             right_node = self.build(nums, mid+1, right)
             tn = TreeNode(nums[mid])
             tn.left = left_node
             tn.right = right_node
             return tn


class Solutions3(object):
        if not nums:
            return None
        else:
            mid = len(nums)//2
            t = TreeNode(nums[mid])
            n1 = nums[:mid]
            n2 = nums[mid + 1:len(nums)]
            t.left = self.sortedArrayToBST(n1)
            t.right = self.sortedArrayToBST(n2)
        return t

