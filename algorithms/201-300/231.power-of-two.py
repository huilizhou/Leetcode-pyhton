class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 我的想法,统计转化为二进制后的1的个数。
        # 例如 2 -10，4-100，8-1000；
        # return bin(n).count("1") == 1 and n > 0

        # 人家的解法
        '''
        2-10,1-01
        2&1=0
        4-100,3,011
        4&3=0
        '''
        return n & (n - 1) == 0 and n > 0

        # # 常规的解法
        # if n <= 0:
        #     return False

        # while n % 2 == 0:
        #     n = n // 2

        # return n == 1


print(Solution().isPowerOfTwo(16))
