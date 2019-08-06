# 最大连续1的个数
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # # 我的想法
        res = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        return max(res, count)

        # 我的写法，时间复杂度比较大
        # if not nums:
        #     return 0
        # dp = [0] * len(nums)
        # if nums[0] == 1:
        #     dp[0] = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == 1 and nums[i - 1] == 1:
        #         dp[i] = dp[i - 1] + 1
        #     elif nums[i] == 1 and nums[i - 1] == 0:
        #         dp[i] = 1
        # return max(dp)


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
