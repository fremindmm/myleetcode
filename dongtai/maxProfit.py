#!/bin/env python 
public int maxProfit(int[] prices) {    
    if(prices==null || prices.length==0) return 0;    
    int local = 0;    
    int global = 0;    
    for(int i=0;i<prices.length-1;i++){  
        local = Math.max(local+prices[i+1]-prices[i],0);    
        global = Math.max(local, global);    
    }    
    return global;    
} 

class Solutions(object):
    def maxProfit(prices):
        if len(prices) == 0 :
            return 0
        local = 0
        global_profit = 0
        for i in xrange(1,len(prices)):
            local = max(local + prices[i]-prices[i-1], 0)
            global_profit = max(local, global_profit)
        return global_profit


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        low, res = prices[0], 0
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            res = max(res, prices[i] - low)
        return res

#找出波谷 找的同时然后不断计算最大利润记录下来 最大利润与其他价格同波谷之差比较 大着即为利润
class mySolutions3(object):
      det maxProfit(prices):
          if len(prices) < 2:
              return 0
          low, ret = prices[0], 0
          for i in xrange(1, len(prices)):
              low = min(low, prices[i])
              res = max(res, prices[i] - low)
          return res

class Solution1(object):
      def maxProfit(prices):
      class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(prices):
        if prices is None  or len(prices) <= 1:
            return 0
        profit = 0
        cur_price_min = 2**31 - 1
        for price in prices:
            profit = max(profit, price - cur_price_min)
            cur_price_min = min(cur_price_min, price)
        return profit

class Solutions2(object):
    def maxProfit(prices):
        result = 0
        for i, price in enumerate(prices):
            if i == 0:
                low = price
            low = min(low, price)
            result = max(price-low, result)
        return result
