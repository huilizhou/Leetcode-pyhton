# 分割等和子集
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)

        # 特判，如果整个数组的和都不是偶数，就无法平分
        s = sum(nums)
        if s & 1 == 1:
            return False

        # 二维 dp 问题：背包的容量
        target = s // 2
        dp = [[False for _ in range(target + 1)] for _ in range(size)]

        # 先写第 1 行：看看第 1 个数是不是能够刚好填满容量为 target
        for i in range(target + 1):
            dp[0][i] = False if nums[0] != i else True
        # i 表示物品索引
        for i in range(1, size):
            # j 表示容量
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


print(Solution().canPartition([1, 5, 11, 5]))
