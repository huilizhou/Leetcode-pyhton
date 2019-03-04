# -*- coding:utf-8 -*-
# 把数组排成最小的数


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers == None or len(numbers) <= 0:
            return ""
        strNum = [str(m) for m in numbers]
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
                    strNum[i], strNum[j] = strNum[j], strNum[i]
        return "".join(strNum)


print(Solution().PrintMinNumber([3, 23, 321]))
