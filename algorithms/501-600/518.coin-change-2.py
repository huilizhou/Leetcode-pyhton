# 零钱兑换II
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        '''
        记录每添加一种面额的零钱，总金额的变化
        例如对于总额5，当只有面额1的零钱时，只有一种可能5*1
        当加了面额为2的零钱时，除了原来那一种可能外，还加上组合了两块的情况。

        '''
        dp = [0] * (amount + 1)
        coins.sort()
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]

        # 人家的解法
        '''
         “完全背包问题”解题有一定的套路和经验。
         1、状态的定义
         dp[i][j]：考虑前i个硬币能凑成总金额j的组合数
         2、状态转移方程
        dp[i][j] = dp[i - 1][j - 0 * coins[i - 1]] + 
        dp[i - 1][j - 1 * coins[i - 1]] +
        dp[i - 1][j - 2 * coins[i - 1]] + 
        ... + 
        dp[i - 1][j - k * coins[i - 1]]

        这里 j - k * coins[i - 1] >= 0。

        '''
        # size = len(coins)
        # dp = [0 for _ in range(amount + 1)]
        # dp[0] = 1

        # for i in range(1, size + 1):
        #     for j in range(amount + 1):
        #         if j - coins[i - 1] >= 0:
        #             dp[j] += dp[j - coins[i - 1]]
        # return dp[amount]


print(Solution().change(5,  [1, 2]))
