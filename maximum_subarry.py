#!/bin/env python

def function(lists):
    max_sum = lists[0]
    pre_sum = 0
    for i in lists:
        if pre_sum < 0:
            pre_sum = i
        else:
            pre_sum += i
        if pre_sum > max_sum:
            max_sum = pre_sum
     return max_sum

def function(nums):
    summ = 0
    max_sum = nums[0]
    for i in nums:
        summ+=i
        if max_sum < summ:
            max_sum = summ
        if summ < 0:
            summ = 0
    return max_sum
