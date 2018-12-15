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
            if a == x:
                return mid
            elif a < x:
                low = mid + 1
            else:
                high = mid - 1

        return high


print(Solution().mySqrt(5))
