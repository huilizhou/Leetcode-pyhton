class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 我一开始没有写nums[:]
        nums[:] = nums[k + 1:] + nums[:k + 1]
