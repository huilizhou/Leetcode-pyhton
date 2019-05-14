# 不同路径
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 我的想法
        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            dp[i][0] = 1
        for j in range(1, m):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

        # 人家的解法计算组合数
        # 实际上是一个组合问题。对于一个mxn的网络来说，我们要直到有多少路径
        # 那么只需要直到在m+n-2个step中，有n-1个向下的step的组合
        # res = 1
        # for i in range(m, m + n - 1):
        #     res *= i
        #     res /= i - m + 1
        # return int(res)

        '''
        import math
        a = math.factorial(m + n - 2)
        b = math.factorial(m - 1) * math.factorial(n - 1)
        return a // b
        '''


print(Solution().uniquePaths(3, 2))
