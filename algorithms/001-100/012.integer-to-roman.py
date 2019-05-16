# 整数转罗马数字
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 方法一：
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX",
                       10: "X", 40: "XL", 50: "L", 90: "XC",
                       100: "C", 400: "CD", 500: "D", 900: "CM",
                       1000: "M"}
        keyset, result = sorted(numeral_map.keys()), []

        while num > 0:
            for key in reversed(keyset):
                while num // key > 0:
                    num -= key
                    result += numeral_map[key]

        return "".join(result)

        # # 方法二:直接将罗马数字的基准摆出来
        # M = ["", "M", "MM", "MMM"]
        # C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        # return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]


print(Solution().intToRoman(2014))
