# 最长上升子序列
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划的解法，时间复杂度为O(n^2)
        # if not nums:
        #     return 0
        # dp = [1] * len(nums)
        # res = 1
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     res = max(res, dp[i])
        # return res

        # 人家的解法
        import bisect
        res = []
        for num in nums:
            if not res or num > res[-1]:
                res.append(num)
            else:
                res[bisect.bisect_left(res, num)] = num
        return len(res)
        # # 二分法O(n log n)很好

        # if not nums:
        #     return 0
        # res = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i] > res[-1]:
        #         res.append(nums[i])
        #     else:
        #         l, r = 0, len(res) - 1
        #         while l <= r:
        #             mid = (l + r) // 2
        #             if nums[i] > res[mid]:
        #                 l = mid + 1
        #             else:
        #                 r = mid - 1
        #         res[l] = nums[i]
        # return len(res)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
