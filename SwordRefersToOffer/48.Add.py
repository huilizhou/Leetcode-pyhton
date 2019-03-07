# -*- coding:utf-8 -*-
# 不用加减乘除做加法


class Solution:
    def Add(self, num1, num2):
        # write code here
        # MAX = 0x7fffffff
        # mask = 0xffffffff
        # while num2 != 0:
        #     num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
        #     num1 = num1 & mask
        #     num2 = num2 & mask
        # return num1 if num1 <= MAX else ~(num1 ^ mask)

        MAX = 0x7fffffff
        mask = 0xffffffff
        while num2 != 0:
            num1, num2 = (num1 ^ num2), (num1 & num2) << 1
            num1 &= mask
            num2 &= mask
        return num1 if num1 <= MAX else ~(num1 & mask)


print(Solution().Add(3, 2))
