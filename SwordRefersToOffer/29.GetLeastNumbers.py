# -*- coding:utf-8 -*-
# 最小的K个数


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        tinput.sort()
        if k > len(tinput):
            return []
        return tinput[:k]
