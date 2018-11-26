class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

        # 直接使用除法符号完成此题
        # res1 = int(abs(dividend) / abs(divisor))
        # if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        #     res1 *= -1
        # if res1 > 2**31 - 1 or res1 < -2**31:

        #     return 2**31 - 1
        # else:
        #     return res1


print(Solution().divide(3, 2))
