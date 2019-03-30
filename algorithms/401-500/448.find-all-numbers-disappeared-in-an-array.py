# 找到所有数组中消失的数字
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        li = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in li]


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
