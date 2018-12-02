class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # 人家的解法
        matrix[:] = map(list, zip(*matrix[::-1]))
        # return [list(reversed(x)) for x in zip(*matrix)]

        # 我的想法
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


print(Solution().rotate(matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
