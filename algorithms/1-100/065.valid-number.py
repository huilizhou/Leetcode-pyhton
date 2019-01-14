# 有效的数字
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 简单的解法
        try:
            float(s)
            return True
        except:
            return False

    # # 人家的解法
    # def valid_num(self, n):
    #     if n.find('.') == -1:
    #         if n.isdigit():
    #             return True
    #         return False
    #     s = n.split('.')
    #     if len(s) > 2:  # 若小数点超过1个
    #         return False
    #     if not s[0] and s[1].isdigit() or not s[1] and s[0].isdigit():
    #         return True
    #     if not s[0] and not s[1]:
    #         return False
    #     return s[0].isdigit() and s[1].isdigit()

    # def isNumber(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     s = s.strip()
    #     if not s:   # 若为空
    #         return False
    #     if s[0] in '-+':     # 若有符号则去符号
    #         s = s[1:]
    #     if s.find(' ') != -1:   # 数字中不允许有空格
    #         return False
    #     if s.find('e') != -1:   # 若包含指数
    #         s = s.split('e')
    #         if len(s) > 2:
    #             return False
    #         if len(s[0]) == 0 or len(s[1]) == 0:    # 指数和非指数部分若至少一个不存在
    #             return False
    #         if s[1][0] in '-+':  # 指数部分若有符号则去符号
    #             s[1] = s[1][1:]
    #         if s[1].find('.') != -1:  # 指数不能有小数点
    #             return False
    #         return self.valid_num(s[0]) and s[1].isdigit()

    #     return self.valid_num(s)


print(Solution().isNumber('21e0'))
