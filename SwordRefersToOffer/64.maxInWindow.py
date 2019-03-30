# -*- coding:utf-8 -*-
# 滑动窗口的最大值


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        slip_max = []
        if num is None or size > len(num) or size == 0:
            return []
        for i in range(len(num) - size + 1):
            slip_max.append(max(num[i:i + size]))
        return slip_max
