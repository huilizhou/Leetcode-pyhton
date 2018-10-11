class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 人家的解法
        # numeral_map = {"I": 1, "V": 5, "X": 10,
        #                "L": 50, "C": 100, "D": 500, "M": 1000}
        # decimal = 0
        # for i in range(len(s)):
        #     if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
        #         decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
        #     else:
        #         decimal += numeral_map[s[i]]
        # return decimal

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


print(Solution().romanToInt("IM"))
