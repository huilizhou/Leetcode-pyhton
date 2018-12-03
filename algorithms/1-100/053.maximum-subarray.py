# 最长子序和
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划，寻找最优子结构

        sum = 0
        max = float("-inf")
        for num in nums:
            sum += num
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
