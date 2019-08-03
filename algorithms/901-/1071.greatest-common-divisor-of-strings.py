# 字符串的最大公因子
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if (str1 + str2) != (str2 + str1):
            return ''

        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a

        num = gcd(len(str1), len(str2))
        return str1[:num]


print(Solution().gcdOfStrings(str1='ABABAB', str2='ABAB'))
