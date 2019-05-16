# 最小路径和
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 我的想法，动态规划的解法
        m = len(grid)  # row
        n = len(grid[0])  # column
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = grid[0][0]
                elif i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[- 1][- 1]


print(Solution().minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
