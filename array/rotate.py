#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/11/12 下午5:03
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : rotate.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """

    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()


class Solution2(object):
    def rotate(self, matrix):
        """
        性能有问题
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        matrix[:] = map(list, zip(*matrix[::-1]))
