class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    num = self.deepSearch(grid, i, j)
                    res = max(res, num)
        return res

    def deepSearch(self, g, i, j):
        g[i][j] = 0
        x = len(g)
        y = len(g[0])
        c = 1
        if i - 1 >= 0 and g[i - 1][j]:  # 上
            c = c + self.deepSearch(g, i - 1, j)
        if j + 1 < y and g[i][j + 1]:  # 右
            c = c + self.deepSearch(g, i, j + 1)
        if i + 1 < x and g[i + 1][j]:  # 下
            c = c + self.deepSearch(g, i + 1, j)
        if j - 1 >= 0 and g[i][j - 1]:  # 左
            c = c + self.deepSearch(g, i, j - 1)
        return c


print(Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
