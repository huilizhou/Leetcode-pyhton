# 位1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 我的想法
        return bin(n).count("1")


print(Solution().hammingWeight(3))
