# 删除排序数组的重复项II
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

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
        return i + 1

        # 人家的解法
        # i = 0
        # for e in nums:
        #     if i < 2 or e != nums[i - 2]:
        #         nums[i] = e
        #         i += 1
        # return i


print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 6]))
