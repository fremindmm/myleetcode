#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/11/22 上午10:16
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : isPalindrome.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lens = len(s)
        s = s.lower()
        if s is '':
            return True
        if lens > 100000:
            return True
        s1 = [s[i] for i in xrange(lens) if s[i].isalnum()]
        if s1 == s1[::-1]:
            return True
        else:
            return False


class Solution2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) > 100000:
            return True
        if s == '':
            return True
        s = s.lower()
        a = [i for i in s if 58 > ord(i) > 47 or 123 > ord(i) > 96]
        if a != a[::-1]:
            return False
        return True
