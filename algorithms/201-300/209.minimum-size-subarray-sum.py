class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #  人家的解法，很有意思
        left, total, res = 0, 0, float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= s:
                total -= nums[left]
                res = min(res, right - left + 1)
                left += 1
        if res == float('inf'):
            return 0
        return res

        # 我的想法
        # minLen = len(nums) + 1
        # for i, _ in enumerate(nums):
        #     sum_all = 0
        #     for j, tmp in enumerate(nums[i:]):
        #         sum_all += tmp
        #         if sum_all >= s:
        #             minLen = min(minLen, j + 1)
        # if minLen == len(nums) + 1:
        #     return 0
        # return minLen


print(Solution().minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
