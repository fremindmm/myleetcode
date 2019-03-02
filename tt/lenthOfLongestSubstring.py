#!/bin/env python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype : int
        """
        temp = 0
        start = 0
        d = {}
        for i in xrange(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            temp = max(i-start+1,temp)
            d[s[i]] = i
        return temp
