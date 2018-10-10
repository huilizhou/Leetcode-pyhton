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
            result = -int(str(x)[::-1])
        if abs(result) <= pow(2, 31):
            return result
        else:
            return 0

# // github
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

# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         ret = 0
#         if x >= 0:
#             ret = int(str(x)[::-1])
#         else:
#             ret = -int(str(abs(x))[::-1])
#         if -pow(2, 31) < ret < pow(2, 31) - 1:
#             return ret
#         else:
#             return 0


print(Solution().reverse(153423646))
