# 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 人家的想法
        # from collections import deque
        # dq = deque()
        # max_numbers = []

        # for i in range(len(nums)):
        #     while dq and nums[i] >= nums[dq[-1]]:
        #         dq.pop()
        #     dq.append(i)
        #     if i >= k and dq and dq[0] == i - k:
        #         dq.popleft()
        #     if i >= k - 1:
        #         max_numbers.append(nums[dq[0]])

        # return max_numbers

        # 我的想法
        # if not nums or k <= 0 or k > len(nums):
        #     return []
        # res = [max(nums[:k])]
        # max_val = res[0]
        # for i in range(k, len(nums)):
        #     if nums[i] > max_val:
        #         max_val = nums[i]
        #     elif nums[i - k] == max_val:
        #         max_val = max(nums[i - k + 1:i + 1])
        #     res.append(max_val)
        # return res

        # 我起初的想法，时间复杂度过大。
        if not nums or k <= 0 or k > len(nums):
            return []
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res


print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
