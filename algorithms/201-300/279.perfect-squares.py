# 完全平方数
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        四平方定理：任何一个正整数都可以表示成不超过四个整数的平方之和。
        推论：满足四数平方和定理的数n(四个整数的情况)，必定满足n=4^a(8b+7)
        '''
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n:
                return (not not a) + (not not b)
            a += 1
        return 3


print(Solution().numSquares(13))
