class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 分析思路
        # 索引和为偶数：元素在第一行，往右走，元素在最后一列，往下走，其他情况往右上走
        # 索引和为奇数，元素在第一列，往下走，元素在最后一行，往右走，其他情况往左下走

        # res = []
        # if not matrix:
        #     return []

        # m = len(matrix)
        # n = len(matrix[0])

        # for level in range(m + n - 1):
        #     if level % 2 == 0:
        #         i = min(m - 1, level)
        #         j = level - i
        #         while i >= 0 and j < n:
        #             res.append(matrix[i][j])
        #             i -= 1
        #             j += 1
        #     else:
        #         j = min(n - 1, level)
        #         i = level - j
        #         while j >= 0 and i < m:
        #             res.append(matrix[i][j])
        #             j -= 1
        #             i += 1
        # return res

        # if len(matrix) == 0:
        #     return []
        # M, N = len(matrix), len(matrix[0])
        # ans = [0] * (M * N)
        # row, col = 0, 0

        # for i in range(M * N):
        #     ans[i] = matrix[row][col]
        #     if (row + col) % 2 == 0:
        #         if col == N - 1:
        #             row += 1
        #         elif row == 0:
        #             col += 1
        #         else:
        #             col += 1
        #             row -= 1
        #     else:
        #         if row == M - 1:
        #             col += 1
        #         elif col == 0:
        #             row += 1
        #         else:
        #             col -= 1
        #             row += 1
        # return ans

        if len(matrix) == 0:
            return []
        M, N = len(matrix), len(matrix[0])
        ans = [0] * (M * N)
        row, col = 0, 0
        for i in range(M * N):
            ans[i] = matrix[row][col]
            if (row + col) % 2 == 0:
                if col == N - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == M - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1
        return ans


print(Solution().findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
))
