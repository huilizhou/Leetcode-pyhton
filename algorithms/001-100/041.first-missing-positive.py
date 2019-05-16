# 缺失的第一个正数
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的想法
        if len(nums) == 0 or min(nums) > 1:
            return 1
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i


print(Solution().firstMissingPositive([0, 1, 2]))
