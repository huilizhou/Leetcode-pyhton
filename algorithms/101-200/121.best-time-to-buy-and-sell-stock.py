# 买卖股票的最佳时机
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 只需遍历一遍数组，用一个变量记录遍历过数中的最小值
        # 然后，每次计算当前值和这个最小值之间的差值即为利润
        # 选择每次较大的利润进行更新

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

        # 人家的解法
        # if not prices or len(prices) <= 1:
        #     return 0
        # min_price = prices[0]
        # res = 0
        # for i in range(1, len(prices)):
        #     if min_price > prices[i]:
        #         min_price = prices[i]
        #     if prices[i] - min_price > res:
        #         res = prices[i] - min_price
        # return res


print(Solution().maxProfit([7, 6, 5, 4, 3, 2, 1]))
