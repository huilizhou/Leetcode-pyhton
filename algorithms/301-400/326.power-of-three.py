# 3的幂
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n // 3
        return n == 1


print(Solution().isPowerOfThree(4))
