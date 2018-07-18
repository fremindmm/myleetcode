#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/7/18 下午7:58
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : Array_deduplication.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

def removeDuplicates(nums):
    for i in nums:
        tmp= nums[nums.index(i) + 1:]
        if i in tmp:
            nums.pop(nums.index(i))
        else:
            continue

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        i = 1
        j = 1
        while(j < len(nums)):
            if(nums[j-1] == nums[j]):
                j += 1
            else:
                nums[i] = nums[j]
                j += 1
                i += 1
        return i

if __name__ == '__main__':
    nums = [1,1,1,1]
    removeDuplicates(nums)
    print nums
