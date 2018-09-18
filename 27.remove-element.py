class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.remove(val)

        # print(nums)
        return len(nums)

        # 人家的解法
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[j] = nums[i]
        #         j += 1
        # for i in range(len(nums) - j):
        #     nums.pop()
        # # print(nums)
        # return j


print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
