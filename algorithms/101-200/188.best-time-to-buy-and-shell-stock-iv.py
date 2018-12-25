class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
    # 人家的解法
    #     if k <= 0 or len(prices) == 0:
    #         return 0
    #     if k > len(prices):
    #         return self.greedy(prices)
    #     l = [[0 for _ in range(k + 1)] for _ in range(len(prices))]
    #     g = [[0 for _ in range(k + 1)] for _ in range(len(prices))]
    #     for i in range(1, len(prices)):
    #         diff = prices[i] - prices[i - 1]
    #         for j in range(1, k + 1):
    #             l[i][j] = max(g[i - 1][j - 1] + max(0, diff),
    #                           l[i - 1][j] + diff)
    #             g[i][j] = max(l[i][j], g[i - 1][j])
    #     return g[-1][-1]

    # def greedy(self, prices):
    #     res = 0
    #     for i in range(1, len(prices)):
    #         res += max(0, prices[i] - prices[i - 1])
    #     return res

        # 人家的解法，当k>n//2时，即转化为交易次数不再受限制
        if k == 0:
            return 0
        if k >= (len(prices) // 2):
            res = 0
            for i in range(1, len(prices)):
                res += max(0, prices[i] - prices[i - 1])
            return res
        buy, sell = [float('inf')] * (k + 1), [0] * (k + 1)
        for price in prices:
            for j in range(1, k + 1):
                buy[j] = min(buy[j], price - sell[j - 1])
                sell[j] = max(sell[j], price - buy[j])
        return sell[-1]


print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))
