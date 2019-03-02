#!/bin/env python
public int climbStairs(int n){

if( n==1) return 1;
int[] dp = new int[n+1];
dp[1] = 1;
dp[2] = 2;
for(int i=3; i<=n; i++)
dp[i] = dp[i-1] + dp[i-2]; 
return dp[n];
}

def climbStairs(int n):
    if n == 1:
        return 1
    dp = {}
    dp[1] = 1
    dp[2] = 2
    for i in xrange(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n ==2: return n
        
        a, b = 1, 2
        while n > 2:
            a, b = b, a + b
            n -= 1
        return b

class Solutions(object):
    def climbStairs(self, n):
        if n == 1 or n == 2 :
            return n
        a, b = 1, 2
        while n > 2:
            a, b = b, a+b
            n -= 1
        return b
