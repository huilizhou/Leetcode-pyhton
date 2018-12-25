# 打家劫舍
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的想法
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        ans = max(nums[0], nums[1])
        while len(nums) > 1:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
                ans = max(ans, dp[i])
            return ans

        # 人家的写法
        # if nums == []:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[1], nums[0])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # return dp[len(nums) - 1]

        # 人家的解法，没想到
        # last, now = 0, 0
        # for i in nums:
        #     last, now = now, max(last + i, now)

        # return now


print(Solution().rob([1, 2, 3, 1]))
