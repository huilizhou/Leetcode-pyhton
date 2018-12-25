# 买卖股票的最佳时机II
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 我的写法
        # max_profit = 0
        # for i in range(len(prices) - 1):
        #     if prices[i + 1] > prices[i]:
        #         max_profit += prices[i + 1] - prices[i]
        # return max_profit

        # 人家的写法
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i - 1])
        return res


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
