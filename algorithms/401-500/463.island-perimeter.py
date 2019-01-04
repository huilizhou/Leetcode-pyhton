class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 我的思路
        # 若不考虑陆地相邻，每块陆地的周长乘以4，若考虑到陆地相邻，使得周长减2
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
        return perimeter


print(Solution().islandPerimeter([[0, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 1, 0, 0],
                                  [1, 1, 0, 0]]
                                 ))
