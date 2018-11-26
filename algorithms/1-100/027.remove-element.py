class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.remove(val)
        return len(nums)

        # 人家的解法，很好理解
        # n = len(nums)
        # i = -1
        # # 定义nums[0...i]为非val的数列
        # j = 0
        # while j <= n - 1:
        #     if nums[j] != val:
        #         i += 1
        #         nums[i] = nums[j]
        #     j += 1
        # return i + 1


print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
