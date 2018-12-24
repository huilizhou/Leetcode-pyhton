# 旋转数组
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 我的想法
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
