# 乘积最大的子序列
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        # 最大的连续子序列乘积可以是正数*正数得到，也可以是负数*负数得到
        # 人家的想法
        # maximum = big = small = nums[0]
        # for n in nums[1:]:
        #     big, small = max(n, n * big, n * small), min(n, n * big, n * small)
        #     maximum = max(maximum, big)
        # return maximum

        # 人家的思路,同上
        '''
        如何快速求出所有以i位置结尾的子数组的最大乘积？
        假设nums[i-1]结尾的最小乘积为min，以nums[i-1]结尾的最大乘积为max。
        那么以nums[i]结尾的最大乘积只能有以下3种可能
        1.max*nums[i]   比如[3,4,5]在计算5的时候
        2.min*nums[i]   比如[-2,3,-4]在计算-4的时候
        3.nums[i]       比如[0.1,0.1,100]
        '''
        if not nums:
            return 0
        max_num = nums[0]
        min_num = nums[0]
        res = nums[0]
        maxEnd = 0
        minEnd = 0
        for i in range(1, len(nums)):
            maxEnd = max_num * nums[i]
            minEnd = min_num * nums[i]
            max_num = max(maxEnd, minEnd, nums[i])
            min_num = min(maxEnd, minEnd, nums[i])
            res = max(res, max_num)
        return res


print(Solution().maxProduct([-3, -1, -4]))
