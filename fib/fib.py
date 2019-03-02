#!/bin/env python 

class solution1(object):
    count = 0
    def fib(n):
        count+=1 #时间复杂度指数级 少用递归
        print count
        if  n < 2:
            return n
        return fib(n-1) + fib(n-2)

class solution2(object):
     def fib(num):
       array = []
       array[0] = 0
       array[1] = 1
       i=2
       while i <= num:
          array[i] = array[i-1] + array[i-2]
          i++       
       return array[num] #O(n)

#f(n) = (1/?5)*(((1+?5)/2)^n - ((1-?5)/2)^n)

#O(n)
def power(a,n):
    ret = a
    for i in xrange(1,n):
        ret *= a
    return ret

#O(lg(n))
def update_power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2:
       ret = update_power(a, n-1/2)
       return ret*ret*a
    else:
       ret = update_power(a,n/2)
       return ret*ret

#look up method O(1)
result = [0,1,1,2,....]
def fib(n)
    return result[n]
def fib_list(value):
    a, b = 0, 1
    result_list = []
    while a < value:
        result_list.append(a)
        a, b = b , a+b
    return result_list

import fibo
fibo.fib(1000)



        



