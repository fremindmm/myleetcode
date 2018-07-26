class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        a=set(nums)
        if nums==[]:
            return False
        else:
            if len(a)!=len(nums):
                return True
            else:
                return False
