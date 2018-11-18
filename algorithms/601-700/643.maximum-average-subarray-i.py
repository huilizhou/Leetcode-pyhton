class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 别人的解法
        # ret, total = sum(nums[:k]), sum(nums[:k])

        # for i in range(k, len(nums)):
        #     total += nums[i] - nums[i - k]
        #     ret = max(ret, total)

        # return ret / k

        # 我的想法与别人想法类似
        cur = sum(nums[0:k])
        max_val = cur
        for i in range(1, len(nums) - k + 1):
            cur += nums[i + k - 1] - nums[i - 1]
            max_val = max(max_val, cur)
        return max_val / k


print(Solution().findMaxAverage([0, 1, 1, 3, 3], k=4))
