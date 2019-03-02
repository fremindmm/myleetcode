#!/bin/env python

class Solutions(object):
        if n < 3:
            return 0
        preme = [1] * n
        preme[0] = preme[1] = 0
        for i in range(2, int(n ** 0.5) +1):
            if preme[i] == 1:
                preme[i*i:n:i] = [0] * len(preme[i*i:n:i])
        return sum(preme)

def getPrimeCount(n):
    num = 0
    if n > 1:
        for i in range(2,n):
            for j in range(2,i):
                if (i % j) ==0:
                    break
            else:
                num += 1
    return num

def countPrime(n):
    if n < 3:
        return 0
    prime = [1] * n
    prime[0] = prime[1] = 0
    for i in range(2, int(n**0.5) +1):
        if prime[i] == 1:
            prime[i*i:n:i] = [0]*len(prime[i*i:n:i])
    return sum(prime)

class Solution2(object):
    def coutPrime(n):
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if prime[i] == 1:
                prime[i*i:n:i] = [0] * len(prime[i*i:n:i])
        return sum(prime)

