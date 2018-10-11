class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        # 人家的解法
        # return all(i == 0 or j == 0 or matrix[i - 1][j - 1] == val
        #            for i, row in enumerate(matrix)
        #            for j, val in enumerate(row))

        # 人家的解法：
        for i, row in enumerate(matrix):
            if i > 0:
                if not matrix[i - 1][:-1] == matrix[i][1:]:
                    return False
        return True
