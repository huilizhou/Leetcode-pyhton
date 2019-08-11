# 丑数
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in [2, 3, 5]:
            while num % i == 0 and num > 0:
                num /= i
        return num == 1


# 思路很简单，这是人家的写法。
        # if num <= 0:
        #     return False

        # while num % 2 == 0:
        #     num //= 2

        # while num % 3 == 0:
        #     num //= 3

        # while num % 5 == 0:
        #     num //= 5

        # return num == 1


print(Solution().isUgly(8))
