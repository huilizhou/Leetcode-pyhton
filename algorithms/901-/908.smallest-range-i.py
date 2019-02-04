# 最小差值i
class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # return abs((max(A) - min(A)) - 2 * K) if max(A) - min(A) - 2 * K > 0 else 0
        return max(0, (max(A) - min(A)) - 2 * K)


print(Solution().smallestRangeI(A=[1, 3, 6], K=3))
