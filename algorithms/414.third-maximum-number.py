class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = list(set(nums))
        sorted_nums = sorted(elements)
        return sorted_nums[-1] if len(elements) < 3 else sorted_nums[-3]


print(Solution().thirdMax([2, 1]))
