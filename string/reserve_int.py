#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2018/11/15 下午5:55
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : reserve_int.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] is not '-':

            x = x[::-1]
            ret = int(x)
            if ret >= 2 ** 31 - 1 or ret <= -2 ** 31:
                return 0
            else:
                return ret
        else:
            ret = int(x[1:][::-1])
            if ret >= 2 ** 31 - 1 or ret <= -2 ** 31:
                return 0
            else:
                return -ret


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        max_int32 = 2 ** 31 - 1
        min_int32 = 0 - 2 ** 31

        flag = 1 if x > 0 else -1
        x = flag * x
        while x > 0:
            mod = x % 10
            r += mod
            r *= 10
            x /= 10
        r = r / 10 * flag
        if r > max_int32 or r < min_int32:
            return 0
        else:
            return r

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(1534236469))
