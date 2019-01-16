class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
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
