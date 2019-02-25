# -*- coding:utf-8 -*-
# 矩形覆盖


class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        first, second, third = 1, 2, 0
        for i in range(3, number + 1):
            third = first + second
            first = second
            second = third
        return third
