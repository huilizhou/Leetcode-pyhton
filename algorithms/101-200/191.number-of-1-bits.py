# 位1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # # 我的想法
        # return bin(n).count("1")

        # 人家的解法
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        return res


print(Solution().hammingWeight(3))
