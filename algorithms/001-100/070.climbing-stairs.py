# 爬楼梯
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 超时，实际上就是一个斐波拉契数列
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # 人家的解法
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


print(Solution().climbStairs(3))
