# 不同路径
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 我的想法计算组合数
        # num = m + n - 2
        # if m < n:
        #     p = m - 1
        # else:
        #     p = n - 1
        # fin = 1
        # for _ in range(p):
        #     fin = fin * num / p
        #     num = num - 1
        #     p = p - 1

        # return round(fin)

        # 人家的想法，牛
        tmp = [[1] * n] * m

        for i in range(1, m):
            for j in range(1, n):
                tmp[i][j] = tmp[i - 1][j] + tmp[i][j - 1]
        return tmp[m - 1][n - 1]


print(Solution().uniquePaths(7, 3))
