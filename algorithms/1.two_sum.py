class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index, value in enumerate(nums):
            if target - value in nums:
                if index != nums.index(target - value):
                    return index, nums.index(target - value)

        return 0

        # dicts = {}
        # for k, v in enumerate(nums):

        #     if target - v in dicts:
        #         return [dicts.get(target - v), k]
        #     dicts[v] = k


print(Solution().twoSum([3, 3], 6))
