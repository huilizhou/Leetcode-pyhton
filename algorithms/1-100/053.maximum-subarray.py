# 最长子序和
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划，寻找最优子结构

        # sum = 0
        # max = float("-inf")
        # for num in nums:
        #     sum += num
        #     if sum > max:
        #         max = sum
        #     if sum < 0:
        #         sum = 0
        # return max

        # 动态规划
        '''
        设dp[i]为以第i个元素结尾且和最大的连续数组。
        假设对于元素i结尾且和最大的连续子数组，实际上要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素
        要么只包含这个元素。
        通过判断dp[i]=max(dp[i-1]+nums[i],nums[i])来做选择。
        由于每次运算只需要前一次结果，可以不像普通的动态规划那样保存之前的结果。
        '''
        if not nums:
            return
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
