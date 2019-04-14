# 3的幂
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 常规解法
        # if n <= 0:
        #     return False

        # while n % 3 == 0:
        #     n = n // 3
        # return n == 1

        # 我的想法
        res = [1]
        sum = 1
        while(sum < 2**31):
            sum *= 3
            res.append(sum)
        if n in res:
            return True
        return False


print(Solution().isPowerOfThree(4))
