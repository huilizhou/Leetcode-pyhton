# 不同路径II 和不同路径I的解法类似
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # 人家的写法
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # if m == 0 or n == 0:
        #     return 0
        # res = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 1:
        #             res[i][j] = 0
        #         else:
        #             if i == 0 and j == 0:
        #                 res[i][j] = 1
        #             elif i == 0 and j > 0:
        #                 res[i][j] = res[i][j - 1]
        #             elif j == 0 and i > 0:
        #                 res[i][j] = res[i - 1][j]
        #             elif i > 0 and j > 0:
        #                 res[i][j] = res[i - 1][j] + res[i][j - 1]
        # return res[m - 1][n - 1]

        # 我的写法
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


print(Solution().uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
