class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = {}
        # for num in nums:
        #     if not num in s:
        #         s[num] = 1
        #     else:
        #         s[num] += 1
        # for key, value in s.items():
        #     if value == 1:
        #         return key

        nums.sort()

        for i in range(len(nums) - 1):
            if (nums[i] != nums[i + 1] and nums[i] != nums[i - 1]):
                return nums[i]
        return nums[len(nums) - 1]


        # # 人家的解法，只有1个数出现1次，余数均出现3次。针对此情况最优
        # return (sum(set(nums)) * 3 - sum(nums)) // 2
print(Solution().singleNumber([2, 2, 2, 1]))
