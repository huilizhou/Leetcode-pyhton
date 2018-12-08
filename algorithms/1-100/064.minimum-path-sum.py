# 最小路径和
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 我的想法
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = grid[0][0]
                elif i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] = min(grid[i][j] + grid[i - 1]
                                     [j], grid[i][j] + grid[i][j - 1])
        return grid[m - 1][n - 1]

        # 人家的写法
        # m = len(grid)
        # n = len(grid[0])
        # res = [[0] * n for _ in range(m)]
        # res[0][0] = grid[0][0]
        # for i in range(1, m):
        #     res[i][0] = grid[i][0] + res[i - 1][0]
        # for j in range(1, n):
        #     res[0][j] = grid[0][j] + res[0][j - 1]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         res[i][j] = min(res[i][j - 1], res[i - 1][j]) + grid[i][j]
        # return res[m - 1][n - 1]


print(Solution().minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
