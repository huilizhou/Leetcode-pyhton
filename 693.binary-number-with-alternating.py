class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)[2:]
        if n == 1:
            return True
        for i in range(1, len(b)):
            if b[i] == b[i - 1]:
                return False
        return True

        # 别人的解法
        # a = bin(n)
        # b = a[2:]
        # if ('11' not in b) and ('00' not in b):
        #     return True
        # else:
        #     return False


print(Solution().hasAlternatingBits(10))
