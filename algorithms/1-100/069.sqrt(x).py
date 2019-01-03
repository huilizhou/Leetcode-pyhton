# 求平方根
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # return int(x**0.5)

        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            a = mid * mid
            if a > x:
                high = mid - 1
            elif a < x:
                low = mid + 1
            else:
                return mid
        return high


print(Solution().mySqrt(10))
