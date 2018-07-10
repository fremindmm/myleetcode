class Solution
    """
    @param n: An interger
    @return: An interger
    def climbStairs(self, n):
        #write your code here
        if n == 0: return 1
        if n == 1: return 1
        
        tmpList = [1,1]
        for i in range(0,n-1):
           x = tmpList[-1] + tmpList[-2]
           tmpList.append(x)
        return tmpList[-1]

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        res = [0 for i in xrange(n)]
        res[0], res[1] = 1, 2
        for i in xrange(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
