# -*- coding:utf-8 -*-
# 数组中只出现一次的数字


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = []
        s = {}
        for i in array:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        for key, value in s.items():
            if value == 1:
                res.append(key)
        return res
