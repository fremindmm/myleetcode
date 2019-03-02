class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        max_sub_sum=nums[0]
        for num in nums:
            sum=sum+num
            if sum >max_sub_sum:
                max_sub_sum=sum
            if sum<0:
                sum=0
        return max_sub_sum


class mySolution1(object):
    def maxSubArray(self, nums):
        length = len(nums)
        for i in xrange(1, length):
            subMaxnum = max(nums[i] + nums[i-1], nums[i])
            nums[i] = subMaxnum
        return max(nums)

class Solution2(object):
    def maxSubArray(self, nums):
        sum = 0
        max_sub_sum = nums[0]
        for n in nums:
            sum = sum + n
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0
        return max_sub_sum
