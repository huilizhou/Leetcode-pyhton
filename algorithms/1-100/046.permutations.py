class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 最简单的做法
        if len(nums) <= 1:
            return [nums[:]]
        import itertools
        return list(itertools.permutations(nums, len(nums)))


print(Solution().permute([1, 2, 3]))
