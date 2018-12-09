# 搜素二维矩阵
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 我的解法，最简单的遍历
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != target:
                    continue
                elif matrix[i][j] == target:
                    return True
        return False

        # 人家的解法
        # if not matrix:
        #     return False
        # row = 0
        # col = len(matrix[0]) - 1
        # while row < len(matrix) and col >= 0:
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] < target:
        #         row += 1
        #     else:
        #         col -= 1
        # return False


print(Solution().searchMatrix(matrix=[

], target=0))
