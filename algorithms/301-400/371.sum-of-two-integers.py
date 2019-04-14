# 不用加法的加法
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        # return sum([a,b])

        # 人家的解法，非科班出生，确实不到位
        while(b != 0):
            s = (a ^ b) & 0xFFFFFFFF
            jinwei = ((a & b) << 1) & 0xFFFFFFFF
            a = s
            b = jinwei
        return a if a < 0X7fffffff else ~(a ^ 0xFFFFFFFF)


print(Solution().getSum(2, 3))
