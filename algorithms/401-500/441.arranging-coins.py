# 排列硬币
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 我的想法
        import math
        return int((-1 + math.sqrt(1 + 8 * n)) // 2)

        # return int(((8 * n + 1) ** 0.5 - 1) / 2)


print(Solution().arrangeCoins(5))
