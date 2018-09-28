class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n

        # return pow(x, n)

        # 人家的解法，位操作。
        # if n < 0:
        #     x = 1 / x
        #     n = -n
        # pow = 1
        # while n:
        #     if n & 1:
        #         pow *= x
        #     x *= x
        #     n >>= 1
        # return pow


print(Solution().myPow(2, -2))
