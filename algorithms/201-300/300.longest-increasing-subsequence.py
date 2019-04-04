# 最长上升子序列
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划的解法，时间复杂度为O(n^2)
        if not nums:
            return 0
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

        # 人家的解法
        # import bisect
        # if not nums:
        #     return 0
        # lis = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i] > lis[-1]:
        #         lis.append(nums[i])
        #     else:
        #         lis[bisect.bisect_left(lis, nums[i])] = nums[i]
        # return len(lis)

        # # 二分法O(n log n)很好
        '''
        dp[i]：所有长度为i+1的递增序列中，最小的那个序列尾数，由定义知dp数组必然是一个递增数组。
        可以用max(dp)，来表示最长递增子序列的长度。

        '''
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
