# 三角形的最大周长
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 我的想法
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i + 1] > A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0


print(Solution().largestPerimeter([3, 6, 2, 3]))
