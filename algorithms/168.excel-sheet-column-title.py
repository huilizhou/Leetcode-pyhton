class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # s实际上就是10进制数转26进制数
        result = ""
        while n > 26:
            result = chr((n - 1) % 26 + 65) + result
            n = (n - 1) / 26
        result = chr(n + 64) + result
        return result

        # rstr = ''
        # while n != 0:
        #     tmp = n % 26
        #     if tmp == 0:
        #         tmp = 26
        #         n -= 26
        #     rstr = chr(ord('A') + tmp - 1) + rstr
        #     n = n // 26
        # return rstr


print(Solution().convertToTitle(27))
