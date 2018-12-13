#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/10/26 上午10:11
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : twoSum.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

#v1 Violent cracking
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[j] == target - nums[i]:
                    return [i, j]

#v2