class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        s = [[0 for _ in range(n)] for _ in range(m)]
        s[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, m):
            if s[i - 1][0] == 0 or obstacleGrid[i][0] == 1:
                s[i][0] = 0
            else:
                s[i][0] = 1

        for j in range(1, n):
            if s[0][j - 1] == 0 or obstacleGrid[0][j] == 1:
                s[0][j] = 0
            else:
                s[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    s[i][j] = 0
                else:
                    s[i][j] = s[i - 1][j] + s[i][j - 1]

        return s[m - 1][n - 1]


print(Solution().uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
