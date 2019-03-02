class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = low + (high-low)//2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1): return 1
        
        l = 1
        r = n
        while l < r:
            mid = (l + r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1 
        return l
