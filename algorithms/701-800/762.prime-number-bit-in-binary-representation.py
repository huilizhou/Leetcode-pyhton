# 二进制表示中质数个数置位
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        res = 0
        for i in range(L, R + 1):
            if bin(i).count('1') in prime:
                res += 1
        return res


print(Solution().countPrimeSetBits(842, 888))
