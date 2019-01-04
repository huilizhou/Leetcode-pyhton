class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.helper(grid, i, j)
                    count += 1
        return count

    def helper(self, grid, i, j):
        grid[i][j] = "0"
        if j > 0 and grid[i][j - 1] == "1":
            self.helper(grid, i, j - 1)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
            self.helper(grid, i, j + 1)
        if i > 0 and grid[i - 1][j] == "1":
            self.helper(grid, i - 1, j)
        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            self.helper(grid, i + 1, j)


print(Solution().numIslands([['1', '0', '1', '0', '1'], [
      '1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]))
