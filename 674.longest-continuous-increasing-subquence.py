class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        ret, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
                ret = max(ret, count)
            else:
                count = 1
        return ret

        # # 人家的解法
        # result, count = 0, 0
        # for i in xrange(len(nums)):
        #     if i == 0 or nums[i-1] < nums[i]:
        #         count += 1
        #         result = max(result, count)
        #     else:
        #         count = 1
        # return result


print(Solution().findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]))
