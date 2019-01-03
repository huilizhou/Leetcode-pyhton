# 寻找峰值
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的想法
        # return nums.index(max(nums))

        # 我的想法
        # if not nums:
        #     return
        # if len(nums) == 1:
        #     return 0
        # if nums[0] > nums[1]:
        #     return 0
        # if nums[-2] < nums[-1]:
        #     return len(nums) - 1
        # for i in range(1, len(nums) - 1):
        #     if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        #         return i


print(Solution().findPeakElement([1]))
