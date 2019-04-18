# 买卖股票的最佳时机III
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
        # buy1 = float("-inf")
        # buy2 = float("-inf")
        # shell1 = 0
        # shell2 = 0
        # for i in range(len(prices)):
        #     # 在该价格点卖出第二笔股票后手里剩的钱，
        #     # 等于上一轮买入第二笔股票后手里剩的钱加上卖出当前股票价格的钱，
        #     # 或者上一轮卖出第二笔股票后手里剩的钱两者中较大的
        #     shell2 = max(shell2, buy2 + prices[i])
        #     # 在该价格点买入第二笔股票后手里剩的钱，
        #     # 等于上一轮卖出第一笔股票后手里剩的钱减去买入当前股票价格的钱，
        #     # 或者上一轮买入第二笔股票后手里剩的钱两者中较大的
        #     buy2 = max(buy2, shell1 - prices[i])
        #     # 在该价格点卖出第一笔股票后手里剩的钱，
        #     # 等于上一轮买入第一笔股票后手里剩的钱加上卖出当前股票价格的钱，
        #     # 或者上一轮卖出第一笔股票后手里剩的钱两者中较大的
        #     shell1 = max(shell1, buy1 + prices[i])
        #     # 在该价格点买入第一笔股票后手里剩的钱，
        #     # 等于初始资金减去买入当前股票价格的钱或者初始资金（不买）中较大的
        #     buy1 = max(buy1, -prices[i])
        # return shell2

        # 人家更加通俗的解法，低位买进，高位卖出
        # a1 = a2 = -float("inf")
        # b1 = b2 = 0
        # for price in prices:
        #     if a1 < -price:
        #         a1 = -price
        #     if b1 < price + a1:
        #         b1 = price + a1
        #     if a2 < b1 - price:
        #         a2 = b1 - price
        #     if b2 < a2 + price:
        #         b2 = a2 + price
        # return b2

        # 我理解完之后的写法，两次遍历
        if len(prices) < 2:
            return 0
        n = len(prices)
        dp1 = [0] * n
        dp2 = [0] * n
        # minval记录在第i天之前(含第i天)prices最小的那一天买进
        minval = prices[0]
        # maxval记录在第i天之后(含第i天)prices最大的那一天卖出
        maxval = prices[-1]

        # 前向
        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], prices[i] - minval)
            minval = min(minval, prices[i])
        # 后向
        for i in range(n - 2, -1, -1):
            dp2[i] = max(dp2[i + 1], maxval - prices[i])
            maxval = max(maxval, prices[i])

        dp = [dp1[i] + dp2[i] for i in range(n)]
        return max(dp)


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
