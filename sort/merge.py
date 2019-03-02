class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m
        p2 = n
        for i in range(m + n - len(nums1)):
            nums1[i + m + n] = 0
        while p1 > 0 or p2 > 0:
            if p1 == 0:
                nums1[p2+p1-1] = nums2[p2-1]
                p2 -= 1
            elif p2 == 0:
                nums1[p2+p1-1] = nums1[p1-1]
                p1 -= 1
            elif nums1[p1-1] > nums2[p2-1]:
                nums1[p2+p1-1] = nums1[p1-1]
                p1 -= 1
            elif nums1[p1-1] <= nums2[p2-1]:
                nums1[p2+p1-1] = nums2[p2-1]
                p2 -= 1

class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n-1] = nums2[:n]
        nums1.sort()

class Solution3(object):
    def merge(self, nums1, m, nums2, n):
        while m>0 and n >0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m = m -1
            else :
                nums1[m+n-1] = nums2[n-1]
                n = n-1
        if n > 0 :
            nums1[:n] = nums2[:n]

class Solution1(object):
    def merge(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        start1 = 0
        start2 = 0
        ret = []
        while True:
            if start1 != len1 or start2 != len2:
                if nums1[start1] < nums2[start2] 
                    ret.append(nums1[start1])
                    start1+=1
                else:
                    ret.append(nums2[start2])
                    start2+=1


# Recursively implementation of Merge Sort
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(L):
    if len(L) <= 1:
        # When D&C to 1 element, just return it
        return L
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    # conquer sub-problem recursively
    return merge(left, right)
    # return the answer of sub-problem


if __name__ == "__main__":
    test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("original:", test)
    print("Sorted:", merge_sort(test))
