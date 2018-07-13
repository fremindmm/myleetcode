class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        min_val = prices[0]
        max_res = 0
        for i in prices[1:]:
            if i < min_val:
                min_val = i
            max_res = max(max_res,i-min_val)
        return max_res


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        min_price = prices[0]
        max_profile = 0
        for i in prices:
            min_price = min(min_price, i)
            max_profile = max(max_profile, i - min_price)
        return max_profile 
