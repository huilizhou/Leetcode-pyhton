# 杨辉三角
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # if not numRows:
        #     return []
        # res = [[1]]
        # for i in range(1, numRows):
        #     res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        # return res[:numRows]

        # 我的想法
        res = []
        for i in range(numRows):
            res.append([1] * (i + 1))
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res


print(Solution().generate(2))
