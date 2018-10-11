class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 常规思路，和判断2的幂次方、判断3的幂次方类似。
        if num <= 0:
            return False

        while num % 4 == 0:
            num = num // 4

        return num == 1


print(Solution().isPowerOfFour(16))
