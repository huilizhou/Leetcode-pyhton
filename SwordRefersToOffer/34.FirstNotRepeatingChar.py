# -*- coding:utf-8 -*-
# 第一次只出现一次的字符


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        res = []
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                res.append(i)
        return min(res) if len(res) != 0 else -1
