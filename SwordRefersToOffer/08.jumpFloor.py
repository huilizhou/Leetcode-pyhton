# -*- coding:utf-8 -*-
# 跳台阶


class Solution:
    def jumpFloor(self, n):
        # write code here
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
