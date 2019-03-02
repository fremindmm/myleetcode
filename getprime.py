#!/bin/bash
from math import sqrt

from cprofile_wrapper import timer


def isprime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in xrange(2, (num)):
        if (num % i) == 0:
            return False
    else:
        return True


def isprime2(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    sqrt_n = int(sqrt(num))

    for i in xrange(2, sqrt_n + 1, 6):
        if (num % i) == 0:
            return False
    return True


def isprime3(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 6 != 1 and num % 6 != 5:
        return False
    sqrt_n = int(sqrt(num))
    for i in xrange(5, sqrt_n + 1, 6):
        if (num % i) == 0 or num % (i + 2) == 0:
            return False
    return True

def sumisprime(num):
    num_str = str(num)
    single_num_list = [int(i) for i in num_str]
    return sum(single_num_list)

@timer
def get_prime_list():
    retlist = [i for i in xrange(1000000, 1000099) if isprime3(i)]
    print retlist
    ret = []
    for num in retlist:
        if isprime(sumisprime(num)):
            if len(ret) == 2:
                return ret
            ret.append(num)
        else:
            continue


# !/usr/bin/python
# -*- coding: utf-8 -*-

MIN = 1000000


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    else:
        if n % 2 == 0 or n % 3 == 0:
            return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_prime_list2():
    i = MIN
    k = 0
    while (k < 2):
        if is_prime(i):
            sum_i = sum(map(int, str(i)))
            if is_prime(sum_i):
                print i
                k += 1
        i += 1


if __name__ == "__main__":
    ret = get_prime_list()
    print str(ret[0])+str(ret[1])


