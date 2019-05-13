# 地下城游戏
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        '''
        自顶向下的方法，会有一个问题，我们需要判断每次到达一个房间后，我们的血量不能是负数。
        如果采用自底向上的思路去做，我们只需要取右和下的最小值（我们需要计算的最小能量），然后减去dungoen[i][j].
        并且保证到达房间前的血量大于等于0就可以了。
        f(i,j)=max(0,min(f(i+1,j),f(i,j+1))-dungeon[i][j])

        '''
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
