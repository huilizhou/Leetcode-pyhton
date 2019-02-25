# -*- coding:utf-8 -*-
# 斐波拉契数列


class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0] + [1] * 39
        for i in range(2, n + 1):
            res[i] = res[i - 2] + res[i - 1]
        return res[n]
