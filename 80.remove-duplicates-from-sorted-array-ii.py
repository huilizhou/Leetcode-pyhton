class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0

        # last, i, same = 0, 1, False
        # while i < len(nums):
        #     if nums[last] != nums[i] or not same:
        #         same = nums[last] == nums[i]
        #         last += 1
        #         nums[last] = nums[i]
        #     i += 1

        # return last + 1

        n = len(nums)
        if (n <= 2):
            return n
        # nums[0...i]是符合要求的
        i = 1
        k = i - 1
        j = i + 1

        while j <= n - 1:
            if (nums[j] != nums[i]) or (nums[j] == nums[i] and nums[j] != nums[k]):
                k = i
                nums[i + 1] = nums[j]
                i += 1
            j += 1

        return i + 1, nums


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 6]))
