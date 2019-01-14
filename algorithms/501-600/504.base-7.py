class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 人家的写法
        if num < 0:
            return '-' + self.convertToBase7(-num)
        result = ''
        while num:
            result = str(num % 7) + result
            num //= 7
        return result if result else '0'

        # 我的想法
        # l = []
        # if num < 0:
        #     s = "-"
        #     num = abs(num)
        # else:
        #     s = ""
        # while num >= 7:
        #     a = num % 7
        #     l.append(a)
        #     num //= 7
        # l.append(num)
        # for i in l[::-1]:
        #     s += str(i)
        # return s


print(Solution().convertToBase7(8))
