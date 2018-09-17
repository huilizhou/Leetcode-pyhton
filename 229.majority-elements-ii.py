class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for v in set(nums):
            if nums.count(v) > len(nums) // 3:
                ret.append(v)
        return ret


print(Solution().majorityElement([3, 3, 2]))
