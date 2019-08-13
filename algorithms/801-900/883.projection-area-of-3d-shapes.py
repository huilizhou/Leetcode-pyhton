class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 俯视图所有非零值的和
        # 主视图，行的最大值之和
        # 左视图，列的最大值之和
        N = len(grid)
        ans = 0

        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]:
                    ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            ans += best_row + best_col
        return ans


print(Solution().projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
