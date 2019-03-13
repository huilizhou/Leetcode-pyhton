# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s = ""
        self.count = {}

    def FirstAppearingOnce(self):
        # write code here
        length = len(self.s)
        for i in range(length):
            if self.count[self.s[i]] == 1:
                return self.s[i]
        return '#'

    def Insert(self, char):
        self.s += char
        if char not in self.count:
            self.count[char] = 1
        else:
            self.count[char] += 1
