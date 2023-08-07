class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        max_profit = 0
        profit_pos = 0
        for buying in range(len(prices)-1):
            if prices[buying] < prices[buying + 1]:
                profit = buying + 1
                if profit > max_profit:
                    max_profit = profit
                    profit_pos = buying + 1
        if profit_pos > 0:
            return profit_pos + 1
        return 0 


