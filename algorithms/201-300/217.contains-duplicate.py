# 存在重复元素
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))


print(Solution().containsDuplicate([1, 2, 3, 4]))
