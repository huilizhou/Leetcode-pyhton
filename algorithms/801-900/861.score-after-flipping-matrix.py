# 翻转矩阵后的得分
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i][0] == 0:
                A[i] = [1 - j for j in A[i]]
        ret = 0
        for i in range(len(A[0])):
            col = [A[j][i] for j in range(len(A))]
            ret += max(sum(col), len(A) - sum(col)) * (2**(len(A[0]) - i - 1))
        return ret


print(Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
