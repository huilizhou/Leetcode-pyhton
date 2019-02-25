# -*- coding:utf-8 -*-
# 二维数组中的查找


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        m = len(array)
        n = len(array[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


print(Solution().Find(5, [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]))
