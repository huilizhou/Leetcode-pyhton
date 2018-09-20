class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我一开始的想法，是找只出现1次的那个数，结果超时
        # for i in nums:
        #     if nums.count(i) == 1:
        #         return i
        nums.sort()

        for i in range(len(nums) - 1):
            if (nums[i] != nums[i + 1] and nums[i] != nums[i - 1]):
                return nums[i]
        return nums[len(nums) - 1]

        # # 0异或任何数不变，任何数与自己异或为0。
        # res = 0
        # for i in nums:
        #     res ^= i
        # return res


print(Solution().singleNumber([2, 2, 1]))
