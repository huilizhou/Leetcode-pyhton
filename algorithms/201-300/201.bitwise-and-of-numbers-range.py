class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 人家的解法，两个数按位与的结果是
        # 相同的部分保存不变，不相同的部分会被置零，
        # 多个数的按位与的结果类似
        # 实际上及求出m和n的高位比特的公共前缀
        # count = 0
        # while n != m:
        #     count += 1
        #     m >>= 1
        #     n >>= 1
        # return n << count

        # 我的想法
        while m < n:
            n &= n - 1
        return n


print(Solution().rangeBitwiseAnd(0, 15))
