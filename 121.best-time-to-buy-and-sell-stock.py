class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 超时了
        # r = []
        # for i in range(len(prices)):
        #     r.append(max(max(prices[i:]) - prices[i], 0))
        # return max(r) if r else 0

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
