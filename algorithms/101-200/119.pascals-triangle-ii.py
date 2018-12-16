# 杨辉三角II
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 我的解法
        res = []
        for i in range(34):
            res.append([1] * (i + 1))
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

        return res[rowIndex]

        # 人家的解法
        # if rowIndex == 0:
        #     return [1]
        # if rowIndex == 1:
        #     return [1, 1]
        # num = [1, 1]
        # for i in range(2, rowIndex + 1):
        #     for j in range(i - 1):
        #         num[j] = num[j] + num[j + 1]
        #     num = [1] + num
        # return num


print(Solution().getRow(3))
