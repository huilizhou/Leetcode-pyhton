class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 双向动态规划，人家的解法
        # if not prices or len(prices) <= 1:
        #     return 0
        # left = [0] * len(prices)
        # right = [0] * len(prices)
        # min1 = prices[0]

        # for i in range(1, len(prices)):
        #     if min1 < prices[i]:
        #         left[i] = max(left[i - 1], prices[i] - min1)
        #     else:
        #         left[i] = left[i - 1]
        #         min1 = prices[i]

        # max1 = prices[len(prices) - 1]
        # for i in range(len(prices) - 2, -1, -1):
        #     if max1 > prices[i]:
        #         right[i] = max(right[i + 1], max1 - prices[i])
        #     else:
        #         right[i] = right[i + 1]
        #         max1 = prices[i]

        # res = 0
        # for i in range(len(prices)):
        #     res = max(res, left[i] + right[i])
        # return res

        # 人家的解法，滚动扫描法
        # 我们只需知道前一个时间点买卖第一第二笔股票的最大收益信息
        # 就可以知道当前的最大收益
        # 在维护4个变量
        buy1 = float("-inf")
        buy2 = float("-inf")
        shell1 = 0
        shell2 = 0
        for i in range(len(prices)):
            shell2 = max(shell2, buy2 + prices[i])
            buy2 = max(buy2, shell1 - prices[i])
            shell1 = max(shell1, buy1 + prices[i])
            buy1 = max(buy1, -prices[i])
        return shell2


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
