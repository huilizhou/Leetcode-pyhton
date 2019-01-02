# 数字转换为16进制数
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # # 人家的想法
        # dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        # hexRes = []
        # if num < 0:
        #     num += 2**32  # 处理负数的方法
        # if num == 0:
        #     return '0'
        # while num > 0:
        #     figure = num % 16
        #     num //= 16
        #     if figure >= 0 and figure <= 9:
        #         hexRes.append(str(figure))
        #     else:
        #         hexRes.append(dict[figure])
        # hexRes = hexRes[::-1]
        # return ''.join(hexRes)  # 数组转换成字符

        # 我的想法
        dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
                8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        res = ''
        if num < 0:
            num = pow(2, 32) + num
        while num >= 16:
            res += dict[num % 16]
            num //= 16
        res += dict[num]
        return res[::-1]


print(Solution().toHex(26))
