# -*- coding:utf-8 -*-
# 字符串的排列
'''
输入一个字符串，按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc，则打印出由字符a,b,c所能排列的所有字符串abc,acb,bca,cab和cba。
全排列的题目
思路：
求整个字符串的全排列，可以看成2步：首先求所有可能出现在第一个位置的字符，
即把第一个字符和后面所有的字符交换

这个时候我们仍把后面的所有字符分为两个部分：后面的字符的第一个字符，以及这个字符之后的所有字符。
'''


class Solution:
    def Permutation(self, ss):
        # write code here
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            temp = self.Permutation(
                ''.join(charList[:i]) + ''.join(charList[i + 1:]))
            for j in temp:
                pStr.append(charList[i] + j)
        return pStr
