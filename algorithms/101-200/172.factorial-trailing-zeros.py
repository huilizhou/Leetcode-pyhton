# 阶乘后的0
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 我的想法，只有2*5，末尾才会有0
        # 2肯定比5多，所以数5的个数
        count = 0
        while n:
            n //= 5
            count += n
        return count


print(Solution().trailingZeroes(0))
