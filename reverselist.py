class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       
        nums_len = len(nums)
        nums[:] = nums[nums_len - k :] + nums[:nums_len - k]
