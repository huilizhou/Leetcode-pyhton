# -*- coding:utf-8 -*-
# 求1 + 2 + 3 + ...+n


class Solution:
    def Sum_Solution(self, n):
        # write code here
        res = 0
        for i in range(1, n + 1):
            res += i
        return res
