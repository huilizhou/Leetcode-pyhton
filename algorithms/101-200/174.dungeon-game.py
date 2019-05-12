# 地下城游戏
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = max(0, -dungeon[i][j])
                elif i == m - 1:
                    dp[i][j] = max(0, dp[i][j + 1] - dungeon[i][j])
                elif j == n - 1:
                    dp[i][j] = max(0, dp[i + 1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(
                        0, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0] + 1


print(Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
