#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/11/27 上午10:04
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : loggestcommprefix.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]
        for i in first:
            ret = [False for j in strs if i not in j]
        for i in ret:
            if i is False:
                index = ret.index(i) - 1
        return ret[:index]


class Solution2(object):
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""
        min_len = 2 ** 31 - 1
        for i in range(len(strs)):
            if strs[i] == "":
                return ""
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
        pos = 0
        while True:
            mark = strs[0][pos]
            flag = True
            for i in range(len(strs)):
                if strs[i][pos] != mark:
                    flag = False
            if not flag:
                break
            pos += 1
            if pos >= min_len:
                break

        return strs[0][:pos]
