# 搜素二维矩阵
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # # 我的解法，最简单的遍历
        # if not matrix:
        #     return False
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] != target:
        #             continue
        #         elif matrix[i][j] == target:
        #             return True
        # return False

        # 我的解法，从第一行最后一列开始进行比较。20190219
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


print(Solution().searchMatrix(matrix=[], target=0))
