class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        count = 0
        i = 1
        while i != n:
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                count += diff
            i += 1
        return count
