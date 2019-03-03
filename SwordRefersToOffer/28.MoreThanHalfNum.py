# -*- coding:utf-8 -*-
# 数组中出现次数超过一半的数字


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        for i in set(numbers):
            if numbers.count(i) > len(numbers) // 2:
                return i
        return 0
