# -*- coding:utf-8 -*-
# 字符串的排列


class Solution:
    def Permutation(self, ss):
        # write code here
        #     if len(ss) <= 0:
        #         return []
        #     res = list()
        #     self.perm(ss, res, '')
        #     uniq = list(set(res))
        #     return sorted(uniq)

        # def perm(self, ss, res, path):
        #     if ss == '':
        #         res.append(path)
        #     else:
        #         for i in range(len(ss)):
        #             self.perm(ss[:i] + ss[i + 1:], res, path + ss[i])
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
                "".join(charList[:i] + "".join(charList[i + 1:])))
            for j in temp:
                pStr.append(charList[i] + j)
            return pStr
