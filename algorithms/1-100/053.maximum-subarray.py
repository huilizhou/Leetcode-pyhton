# 最长子序和
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划，寻找最优子结构
        '''
        如果nums中没有正数，产生的最大累加和一定是数组中的最大值
        如果nums中有正数，从左遍历nums。用cur记录每一步的累加和，遍历到正数，cur增加，遍历到负数，cur减小。
        当cur<0时，说明累加到当前数出现了小于0的结果，那么累加的部分不能作为产生累加和的子数组的左边部分，此时令cur=0
        表示重新从下一个数开始累加。
        当cur>=0时，每一次累加都可能是最大累加和，所以用另外一个变量max_value全程跟踪记录cur出现的最大值即可。

        '''

        cur = 0
        max_value = float("-inf")
        for num in nums:
            cur += num
            max_value = max(cur, max_value)
            if cur < 0:
                cur = 0
        return max_value

        '''
        # 动态规划
        # 设dp[i]为以第i个元素结尾且和最大的连续数组。
        # 假设对于元素i结尾且和最大的连续子数组，实际上要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素
        # 要么只包含这个元素。
        # 通过判断dp[i]=max(dp[i-1]+nums[i],nums[i])来做选择。
        # 由于每次运算只需要前一次结果，可以不像普通的动态规划那样保存之前的结果。 
        '''

        # if not nums:
        #     return
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        # return max(dp)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
