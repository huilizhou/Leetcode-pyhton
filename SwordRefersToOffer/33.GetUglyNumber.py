# -*- coding:utf-8 -*-
# 丑数


class Solution:
    ugly = sorted([2**a * 3**b * 5**c for a in range(32)
                   for b in range(20) for c in range(14)])

    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        return Solution.ugly[index - 1] if index > 0 else None
