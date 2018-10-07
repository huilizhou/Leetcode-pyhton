class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)


print(Solution().searchInsert([1, 3, 5, 6], 7))
