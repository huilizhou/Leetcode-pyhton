# -*- coding:utf-8 -*-
# 变态跳台阶


class Solution:
    def jumpFloorII(self, number):
        # write code here
        # return pow(2, number - 1)
        if number <= 2:
            return number
        total = 1
        for _ in range(1, number):
            total *= 2
        return total
