#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/11/16 下午5:52
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : firstuniq.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in s:
            if i not in s[s.index(i):]:
                return s.index(i)
        return -1

#性能太差
class Solution(object):
    def firstUniqChar(self, s):
        if s == '':
            return -1
        length = len(s)
        p = length
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            start = s.find(char)
            end = s.rfind(char)
            if start != -1 and start == end:
                p = min(p, start)
        if p == length:
            return -1
        return p

