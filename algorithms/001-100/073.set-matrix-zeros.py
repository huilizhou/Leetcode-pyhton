# 矩阵置零
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 我的想法
        m = len(matrix)
        n = len(matrix[0])
        row = []
        col = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in col:
                matrix[i][j] = 0

        # 人家的解法
        # m = len(matrix)
        # n = len(matrix[0])
        # idx = []
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             idx.append((i, j))

        # while idx:
        #     i, j = idx.pop()
        #     matrix[i] = [0] * n
        #     for k in matrix:
        #         k[j] = 0


print(Solution().setZeroes([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]))
