class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        res = list()
        if l1 <= l2:
            s = nums1
            l = nums2
        else:
            l = nums1
            s = nums2
        for i in l:
            if i in s:
                res.append(i)
                s.remove(i)
        return res
