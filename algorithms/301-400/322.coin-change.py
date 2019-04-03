# 零钱兑换
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        """
        首先0/1 背包的动态规划，就是取与不取的问题，
        dp[i]表示金额为i需要最少的金额i是多少，
        对于任意的金额j，dp[j]=min(dp[j],dp[j-coin]+1)，如果j-coin存在的话
        20190317头条笔试第一题
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1


print(Solution().coinChange([1, 2, 5, 10], 30))
