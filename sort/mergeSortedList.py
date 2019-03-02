class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #if m+n == 0:
        #    return None
        #if m == 0 and n != 0:
        #    return nums2.sort()
        #if n == 0 and m !=0:
        #    return nums1.sort()
        #nums1 = (nums1+nums2).sort()
        #for i in nums1:
        #    if i != 0:
        #        index = nums1.index(i)
        #return ret[index+1:]
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            if n > 0:
                nums1[:n] = nums2[:n]
                

nums1 = [4,5]   2, nums2[1,2,3] 3


        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:#若nums1中最后一个元素大于nums2[]中最后一个元素
                nums1[m+n-1]=nums1[m-1]#则扩展后的列表最后一个元素是俩元素中最大的
                m-=1       #nums1中元素-1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if n>0:#若nums1完了，nums2还没完
            nums1[:n]=nums2[:n]

