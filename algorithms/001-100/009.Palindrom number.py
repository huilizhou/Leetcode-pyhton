# 回文数字
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return  str(x)[::-1] == str(x)

        # 大神的解法
        # import math
        # r = list(map(lambda i: int(10**-i * x % 10),
        #              range(int(math.log10(x)), -1, -1))) if x > 0 else [0, x]
        # return r == r[::-1]

        # 不转化成字符串
        if x == 0:
            return True
        elif x < 0 or (x != 0 and x % 10 == 0):
            return False
        else:
            res = 0
            while x > res:
                res = 10 * res + x % 10
                x //= 10
                if x == res or x == res // 10:
                    return True
            return False


print(Solution().isPalindrome(-121))
