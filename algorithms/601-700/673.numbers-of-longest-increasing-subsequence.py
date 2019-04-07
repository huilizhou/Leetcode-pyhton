# 最长递增子序列的个数
class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] <= dp[j]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
        return sum(c for i, c in enumerate(count) if dp[i] == max(dp))


print(Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
