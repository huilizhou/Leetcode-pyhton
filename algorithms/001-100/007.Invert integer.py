# 反转整数
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0

        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(abs(x))[::-1])
        if abs(result) <= pow(2, 31):
            return result
        else:
            return 0

# 别人的写法
# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         pos = True if x >= 0 else False
#         x = int(str(abs(x))[::-1])
#         x = x if pos else -x
#         return x if abs(x) <= 0x7fffffff else 0


# print(Solution().reverse(-120))


print(Solution().reverse(-12))
