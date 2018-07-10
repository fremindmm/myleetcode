#!/bin/env python

def sqrt(x):
   i = 0
   j = x/2 + 1
   while(i <= j):
      mid = (i+j)/2
      sq = mid*mid
      if sq == x:
          return mid
      elif sq < x:
          i = mid + 1
      else:
          j = mid -1   
   return j
def sqrt(x):
    return int(x**0.5)
