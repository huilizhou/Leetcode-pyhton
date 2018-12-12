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

        # 我的想法
        res = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if count > res:
                res = count
        return res


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
