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
                dp[i] = dp[i] + dp[i - coin]
        return dp[amount]


print(Solution().change(5,  [1, 2]))
