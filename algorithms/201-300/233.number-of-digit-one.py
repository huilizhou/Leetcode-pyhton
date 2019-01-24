class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 人家的想法
        # if n <= 0:
        #     return 0
        # if n < 10:
        #     return 1
        # l = len(str(n))
        # x = pow(10, l - 1)
        # top = n // x
        # rem = n % x
        # if top == 1:
        #     return rem + 1 + self.countDigitOne(x - 1) + self.countDigitOne(rem)
        # else:
        #     return x + top * self.countDigitOne(x - 1) + self.countDigitOne(rem)

        # # 我的想法
        def helper(n):
            if n <= 0:
                return 0
            p = 1
            l = 0
            while p * 10 <= n:
                p *= 10
                l += 1
            d1 = n // p
            res = p * l // 10 * d1
            if d1 > 1:
                res += p
            else:
                res += n % p + 1
            return res + helper(n % p)
        return helper(n)


print(Solution().countDigitOne(12))
