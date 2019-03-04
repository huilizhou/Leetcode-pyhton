# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        sum = 0
        max = float("-inf")
        for num in array:
            sum += num
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max


print(Solution().FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2]))
