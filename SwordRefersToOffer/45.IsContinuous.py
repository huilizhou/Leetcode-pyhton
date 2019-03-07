# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) < 5:
            return False
        max_num = -1
        min_num = 14
        flag = 0
        for number in numbers:
            if number < 0 or number > 13:
                return False
            if number == 0:
                continue
            if (flag >> number) & 1 == 1:
                return False
            flag |= 1 << number
            if number < min_num:
                min_num = number
            if number > max_num:
                max_num = number
            if max_num - min_num >= 5:
                return False
        return True
