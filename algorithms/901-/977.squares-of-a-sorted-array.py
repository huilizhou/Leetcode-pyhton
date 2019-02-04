# 有序数组的平方
class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for i in A:
            res.append(i * i)
        res.sort()
        return res


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
