# -*- coding:utf-8 -*-
# 构建乘积数组


class Solution:
    def multiply(self, A):
        # write code here
        result = [1] * len(A)
        tmp = 1
        for i in range(1, len(A)):
            result[i] = result[i - 1] * A[i - 1]
        for j in range(len(A) - 2, -1, -1):
            tmp = tmp * A[j + 1]
            result[j] = result[j] * tmp
        return result
