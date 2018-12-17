# 三角形最小路径和
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 我的解法，动态规划。倒序
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])
        return triangle[0][0]

        #  人家的解法，很厉害
        # f = [0] * (len(triangle) + 1)
        # for row in triangle[::-1]:
        #     for i in range(len(row)):
        #         f[i] = row[i] + min(f[i], f[i + 1])
        # return f[0]


print(Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
