class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # 小强哥github上的代码
        # result, local_max = 0, 0
        # for n in nums:
        #     local_max = local_max + 1 if n else 0
        #     result = max(result, local_max)
        # return result

        count, res = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        res = max(res, count)
        return res


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
