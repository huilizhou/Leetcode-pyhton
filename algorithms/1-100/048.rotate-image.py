class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        return [list(reversed(x)) for x in zip(*matrix)]


print(Solution().rotate(matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
