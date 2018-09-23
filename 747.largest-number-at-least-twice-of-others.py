class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        else:
            a = max(nums)
            a_index = nums.index(a)
            nums.remove(a)
            b = max(nums)
            if a >= 2 * b:
                return a_index
            else:
                return -1


print(Solution().dominantIndex([1, 2, 6]))
