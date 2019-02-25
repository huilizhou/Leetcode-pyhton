# -*- coding:utf-8 -*-
# 替换空格


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.replace(' ', '%20')
        return s


print(Solution().replaceSpace("We Are Happy"))
