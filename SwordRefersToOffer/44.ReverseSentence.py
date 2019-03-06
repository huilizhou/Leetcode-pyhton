# -*- coding:utf-8 -*-
# 翻转单词顺序列


class Solution:
    def ReverseSentence(self, s):
        # write code here
        return ' '.join(s.split(" ")[::-1])
