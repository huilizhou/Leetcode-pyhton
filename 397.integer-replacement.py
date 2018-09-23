class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 我的解法，有问题
        # count = 0
        # while n != 1:
        #     if n % 2 == 0:
        #         n /= 2
        #         count += 1
        #     else:
        #         n = n + 1 or n - 1
        #         count += 1
        # return count

        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn


print(Solution().integerReplacement(7))
