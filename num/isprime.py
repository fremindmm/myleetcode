#!/bin/env python
#-*-coding:utf-8-*-
import sys
sys.path.append('../')
#from cprofile_wrapper import timer
profile = __import__("cprofile_wrapper",fromlist = True)
timer = getattr(profile, 'timer')
class Solution2(object):
    def isPrime(self,num):
        if num <= 1:
            return False
        if num == 2 or num == 3:
            return True
        for i in xrange(2, (num)):
            if (num % i) == 0:
                return False
        else:
            return True
    def get_prime_list(self,start,end):
        return [x for x in xrange(start, end) if self.isPrime(x) ]

class Solutions(object):
    def isPrime(self,n):
        """:type n: int
           :rtype: list
        """
        if n > 1:
            for i in xrange(2,n):
                if n%i == 0:
                    break
            else:
                 return True
        else:
            return False
    def get_prime_list(self,start,end):
        return [x for x in xrange(start, end) if self.isPrime(x) ]

class Solution3(object):
    """:type n: int
       :rtype: list
    """
    def isPrime(self, num):
        if num <= 3:
            return num>1
        for i in xrange(2, num):
            if num % i == 0:
                return False
        else:
            return True
    @timer
    def get_prime_list(self,start,end):
        return [x for x in xrange(start, end) if self.isPrime(x) ]

class Solution4(object):
    """:type n: int
       :rtype: list
    """
    def isPrime(self, num):
        import math
        if num <= 3:
            return num>1
        end = int(math.sqrt(num) + 1)
        for i in xrange(2, end):
            if num % i == 0:
                return False
        else:
            return True
    @timer
    def get_prime_list(self,start,end):
        return [x for x in xrange(start, end) if self.isPrime(x) ]

class Solution5(object):
    """:type n: int
       :rtype: list
    """
    def isPrime(self, num):
        import math
        if num <= 3:
            return num>1
        #不在6两侧的数一定不是质数
        if num % 6 !=1 and num % 6 != 5:
            return False
        end = int(math.sqrt(num) + 1)
        for i in xrange(5, end, 6):
            if num % i == 0 or num % (i+2) == 0:
                return False
        else:
            return True
    @timer
    def get_prime_list(self,start,end):
        return [x for x in xrange(start, end) if self.isPrime(x) ]

#此方法超时不可用
class Solution7(object):
    """:type n: int
       :rtype: list
    """
    def isPrime(self, num):
        ret = 0
        if num <=1:
            return False
        if num == 2 or num == 3:
            return True
        for i in range(2, num):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                return True
    @timer
    def get_prime_list(self,start,end):
        return [x for x in xrange(start, end) if self.isPrime(x) ]
       
    

class Solution6(object):
    """:type n: int
       :rtype: list
    """
    def isPrime(self, num):
        if num <= 3:
            return num>1
        #不在6两侧的数一定不是质数
        if num % 6 !=1 and num % 6 != 5:
            return False
        num_sqrt = int(num**0.5)
        end = int(num_sqrt + 1)
        for i in xrange(5, end, 6):
            if num % i == 0 or num % (i+2) == 0:
                return False
        else:
            return True
    @timer
    def get_prime_list(self,start,end):
        return [x for x in xrange(start, end) if self.isPrime(x) ]
if __name__ == "__main__":
    s3 = Solution3()
    print s3.get_prime_list(1,10000)
    s4 = Solution4()
    print s4.get_prime_list(1,100000)
    s5 = Solution5()
    print s5.get_prime_list(1,100000)
    s6 = Solution6()
    print s6.get_prime_list(1,100000)
    #s7 = Solution7()
    #print s7.get_prime_list(1,100000)
     
             
