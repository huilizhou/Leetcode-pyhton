# -*- coding:utf-8 -*-
# 和为S的连续正数序列


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        low, high = 1, 2
        while low < high:
            curSum = (low + high) * (high + 1 - low) // 2
            if curSum == tsum:
                tmp = []
                for i in range(low, high + 1):
                    tmp.append(i)
                result.append(tmp)
                low += 1
            elif curSum < tsum:
                high += 1
            else:
                low += 1
        return result
