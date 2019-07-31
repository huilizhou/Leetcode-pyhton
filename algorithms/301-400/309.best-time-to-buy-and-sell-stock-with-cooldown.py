# 最佳买卖股票时机含有冷冻期
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0, 0] for _ in range(len(prices) + 2)]
        dp[0][1] = -float('inf')
        for i in range(1, len(prices) + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 2][0] - prices[i - 1], dp[i - 1][1])
        return dp[len(prices)][0]


print(Solution().maxProfit([1, 2, 3, 0, 2]))
