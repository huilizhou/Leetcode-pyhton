# -*- coding:utf-8 -*-
# 二进制中1的个数


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = n & (n - 1)
        return count


print(Solution().NumberOf1(3))
