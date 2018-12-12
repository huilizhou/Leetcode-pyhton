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
        # left, right = 0, 0
        # total_sum = 0
        # res = len(nums) + 1
        # while left < len(nums):
        #     if right < len(nums) and total_sum < s:
        #         total_sum += nums[right]
        #         right += 1
        #     else:
        #         total_sum -= nums[left]
        #         left += 1

        #     if total_sum >= s:
        #         res = min(res, right - left)
        # if res == len(nums) + 1:
        #     return 0
        # return res


print(Solution().minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
