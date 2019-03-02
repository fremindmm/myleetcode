#!/bin/env python 

class Solutions():
    @staticmethod
    def cout_and_return(string):
        #error -n not in
        return bin(int(string,10)).count('1')

class Solutions2():
    @staticmethod
    def cout_and_return(string):
        return bin(int(string,10) & 0xf11111111).count('1')

class Solutions3():
    @staticmethod
    def NumberOf1(self, n):
        count = 0
        while n&0xffffffff != 0:
            count += 1
            n = n & (n-1)
        return count

if __name__ == "__main__":
    print  Solutions.cout_and_return('-1')
    print  Solutions2.cout_and_return('-1')
    print  Solutions3.NumberOf1('-1')
