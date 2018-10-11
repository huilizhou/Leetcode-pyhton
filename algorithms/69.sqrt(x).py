import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # return int(math.sqrt(x))
        return int(x**0.5)


print(Solution().mySqrt(5))
