class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 人家的解法1
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        return nums

        # 下面两种解法是类似的。
        # size, Index = len(nums), 0
        # for i in range(size):
        #     if nums[i] != 0:
        #         nums[Index] = nums[i]
        #         Index += 1
        # nums[Index:] = [0] * (size - Index)

        # 这种解法是先将非零项全部提取出来，最后接上为0的元素。
        # 直观的解法是建立新的数组，不符合题意的要求。

        # n = len(nums)
        # i = -1
        # j = 0
        # # nums[0...i]表示非零元素的数列，初始值为i=-1
        # while j <= n - 1:
        #     if nums[j] != 0:
        #         i += 1
        #         nums[i] = nums[j]
        #     j += 1
        # for k in range(i + 1, n):
        #     nums[k] = 0


print(Solution().moveZeroes([1, 0, 2, 0, 3, 5, 9]))
