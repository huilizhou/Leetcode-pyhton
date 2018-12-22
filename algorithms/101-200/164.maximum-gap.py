# 最大间距
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的想法
        if len(nums) <= 1:
            return 0
        nums.sort()
        res = 0
        for i in range(len(nums) - 1):
            res = max(nums[i + 1] - nums[i], res)
        return res


print(Solution().maximumGap([3, 6, 9, 1]))
