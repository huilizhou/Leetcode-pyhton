class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 人家的解法
        # pos = 0
        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[i], nums[pos] = nums[pos], nums[i]
        #         pos += 1

        size, Index = len(nums), 0
        for i in range(size):
            if nums[i] != 0:
                nums[Index] = nums[i]
                Index += 1
        nums[Index:] = [0] * (size - Index)
