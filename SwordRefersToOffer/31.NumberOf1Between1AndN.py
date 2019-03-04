# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res, a, b = 0, 1, 1
        while n > 0:
            res += (n + 8) // 10 * a + (n % 10 == 1) * b
            b += (n % 10) * a
            a *= 10
            n //= 10
        return res
