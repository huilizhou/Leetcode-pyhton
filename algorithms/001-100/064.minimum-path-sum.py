# 最小路径和
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 我的想法，动态规划的解法
        # m = len(grid)  # row
        # n = len(grid[0])  # column
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             grid[i][j] = grid[0][0]
        #         elif i == 0 and j > 0:
        #             grid[i][j] += grid[i][j - 1]
        #         elif j == 0 and i > 0:
        #             grid[i][j] += grid[i - 1][j]
        #         elif i > 0 and j > 0:
        #             grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        # return grid[- 1][- 1]

        # 我的想法
        '''
        状态定义dp为mxn矩阵，其中dp[i][j]的值代表直到走到(i,j)的最小路径和。

        转移方程，只能向右或者向下走，即当前单元格(i,j)只能是左方单元格(i-1,j)或上方单元格(i,j-1)走到。
        因此只需要考虑矩阵左边界和上边界。

        '''
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)]for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


print(Solution().minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
