class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        med = (len(nums) - 1) // 2
        nums[0::2], nums[1::2] = nums[med::-1], nums[:med:-1]
