# 不同路径II 和不同路径I的解法类似
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # 人家的解法
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # if m == 0 or n == 0:
        #     return 0
        # res = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 1:
        #             continue
        #         else:
        #             if i == 0 and j == 0:
        #                 res[i][j] = 1
        #             else:
        #                 if i - 1 >= 0:
        #                     res[i][j] += res[i - 1][j]
        #                 if j - 1 >= 0:
        #                     res[i][j] += res[i][j - 1]
        # return res[m - 1][n - 1]

        # 我的想法
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        res[i][j] = 1
                    elif i == 0 and j > 0:
                        res[i][j] = res[i][j - 1]
                    elif j == 0 and i > 0:
                        res[i][j] = res[i - 1][j]
                    elif i > 0 and j > 0:
                        res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[m - 1][n - 1]


print(Solution().uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
