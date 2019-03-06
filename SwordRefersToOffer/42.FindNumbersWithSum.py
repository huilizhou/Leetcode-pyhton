# -*- coding:utf-8 -*-
# 和为S的两个数字


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) <= 1:
            return []
        left, right = 0, len(array) - 1
        while left < right:
            if array[left] + array[right] == tsum:
                return array[left], array[right]
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                right -= 1
        return []
