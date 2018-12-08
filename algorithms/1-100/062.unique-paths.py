# 不同路径
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 我的想法

        res = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    res[i][j] = 1
                elif i == 0 and j > 0:
                    res[i][j] = res[i][j - 1]
                elif j == 0 and i > 0:
                    res[i][j] = res[i - 1][j]
                elif i > 0 and j > 0:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[m - 1][n - 1]

        # 人家的解法计算组合数
        # res = 1
        # for i in range(m, m + n - 1):
        #     res *= i
        #     res /= i - m + 1
        # return int(res)

        # # 人家的想法，牛，动态规划
        # tmp = [[1] * n] * m
        # for i in range(1, m):
        #     for j in range(1, n):
        #         tmp[i][j] = tmp[i - 1][j] + tmp[i][j - 1]
        # return tmp[m - 1][n - 1]


print(Solution().uniquePaths(7, 3))
