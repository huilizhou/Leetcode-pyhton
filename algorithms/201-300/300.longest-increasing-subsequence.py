# 最长上升子序列
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划的解法，过段时间整理人家的解法
        if not nums:
            return 0
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
