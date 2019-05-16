# 罗马数字转整数
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 罗马数字中小的数字，小的数字在大的数字左边，则相减。

        roman = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        a = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                a -= roman[s[i]]
            else:
                a += roman[s[i]]
        p = a + roman[s[-1]]
        return p


print(Solution().romanToInt("XCIX"))
