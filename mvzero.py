#!/bin/env python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in nums:
            if i == 0:
                nums.pop(i)
                count+=1
            else:
                continue
        zerolist=[0 for i in range(count)]
        return nums + zerolist

class Solution(object):
    def moveZeroes(self, nums):
        a = 0
        length = len(nums)
        while a < len(nums):
            while nums != [] and nums[a] == 0:
            # if nums[a] == 0:
                nums[a: a+1] = []
                if a >= len(nums):
                    break
            a += 1
        nums += [0]*(length-len(nums))
